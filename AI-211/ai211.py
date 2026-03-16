import numpy as np


def inverse(A):
    n = len(A)
    A = np.hstack((A, np.eye(n)))
    
    for i in range(n):
        max_row = np.argmax(np.abs(A[i:, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        
        A[i] = A[i] / A[i, i]
        
        for j in range(i + 1, n):
            A[j] = A[j] - A[j, i] * A[i]
    
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            A[j] = A[j] - A[j, i] * A[i]
    
    return A[:, n:]    


def norm2(v):
    return np.sqrt(v.T @ v)[0][0]


def qr_householder(A):
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy().astype(float)

    for i in range(min(m, n)):
        a = R[i:, i][:, np.newaxis]
        e = np.zeros_like(a)
        e[0] = 1
        v = a + np.sign(a[0]) * norm2(a) * e
        if not norm2(v) == 0:
            u = v / norm2(v)
            H = np.eye(m-i) - 2 * u @ u.T
            R[i:, i:] = H @ R[i:, i:]
            Q[:, i:] = Q[:, i:] @ H
        else:
            break

    return Q, R


def gram_schmidt(unit_vectors, /, *, v_init=None):
    if str(type(v_init)) == '<class \'NoneType\'>':
        # print('Performed Gram Schmidt')
        v_init = np.zeros_like(unit_vectors[0])
        v_init[len(unit_vectors) - 1] = 1
    else:
        v_init = v_init
    projections = sum([v_init.T @ u * u for u in unit_vectors])
    v_init -= projections
    v = v_init / norm2(v_init)
    
    return v


def eig(A, tol=1e-6, n_iter=500):
    n = A.shape[0]
    Q_total = np.eye(n)
    A_i = A.copy()

    for i in range(n_iter):
        # print(f'Householder iteration: {i}')
        Q, R = qr_householder(A_i)
        A_next = R @ Q
        Q_total = Q_total @ Q
        if i % 10 == 0:
            if np.allclose(A_i, A_next, atol=tol):
                print('Convergence')
                break
        A_i = A_next

    eigenvalues = np.diag(A_i)
    eigenvectors = Q_total

    sort_by_eigenval = np.argsort(eigenvalues)[::-1]

    return (
        eigenvalues[sort_by_eigenval], 
        eigenvectors[:, sort_by_eigenval]
    )


def svd(A, tol=1e-6, n_iter=500):
    # print('Now performing SVD')
    m, n = A.shape
    ATA = A.T @ A
    U = np.zeros((m, m))
    S = np.zeros((m, n))
    V = np.zeros((n, n))

    eigenvalues, eigenvectors = eig(ATA, tol, n_iter)
    sigma = np.sqrt(np.maximum(eigenvalues, 0))
    V = eigenvectors
    
    for i in range(min(m, n)):
        S[i, i] = sigma[i]
        if sigma[i] != 0:
            U[:, i] = (1/sigma[i]) * A @ V[:, i]
        elif sigma[i] == 0:
            U[:, i][:, np.newaxis] = gram_schmidt(
                [U[:, j][:, np.newaxis] for j in range(i)]
            )
            # print(f'Filled up col {i} of U.')
 
    if m > n:
        for i in range(n + 1, m):
            U[:, i][:, np.newaxis] = gram_schmidt(
                [U[:, j][:, np.newaxis] for j in range(i)]
            )
            # print(f'Filled up col {i} of U.')

    return U, S, V.T


def scale_data(A):
    mean_val = np.mean(A)
    A_centered = A - mean_val
    min_val = np.min(A_centered)
    max_val = np.max(A_centered)

    return (2 * (A_centered - min_val) / (max_val - min_val)) - 1


class SimpleANN:
    def __init__(
            self, 
            input_layer_size, 
            hidden_layer_size, 
            num_labels,
            alpha=0.0005, 
            n_iters=100
        ):
        self.hidden_layer_size = hidden_layer_size
        self.input_layer_size = input_layer_size
        self.num_labels = num_labels
        self.alpha = alpha
        self.n_iters = n_iters

        self.initialize_weights()

        self.losses = []
        self.epochs = 0
    
    def initialize_weights(self):
        np.random.seed(42)
        self.theta1 = np.random.rand(
            self.hidden_layer_size, 
            self.input_layer_size + 1
        )
        self.theta1 = self.theta1 - 0.5
        self.theta2 = np.random.rand(
            self.num_labels, 
            self.hidden_layer_size + 1
        )
        self.theta2 = self.theta2 - 0.5

    @staticmethod
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))
    
    @staticmethod
    def sigmoid_grad(z):
        sig = SimpleANN.sigmoid(z)
        return sig * (1 - sig)
    
    def forward_propagate(self, X):
        m = X.shape[0]
        a1 = np.c_[np.ones(m), X]
        z2 = a1 @ self.theta1.T
        a2 = np.c_[np.ones(m), self.sigmoid(z2)]
        z3 = a2 @ self.theta2.T
        a3 = self.sigmoid(z3)
        return a1, z2, a2, z3, a3

    def compute_cost(self, a3, y_matrix, m):
        J = (1 / (2 * m)) * np.sum((a3 - y_matrix) ** 2 )
        return J

    def back_propagation(self, a1, z2, a2, z3, a3, y_matrix):
        m = a1.shape[0]
        dj_da3 = (1/m) * (a3 - y_matrix)
        da3_dz3 = self.sigmoid_grad(z3)
        dz3_da2 = self.theta2
        da2_dz2 = self.sigmoid_grad(z2)
        dz2_dw1 = a1
        dz3_dw2 = a2

        dc_dw1 = (((dj_da3 * da3_dz3 @ dz3_da2)[:, 1:]) * da2_dz2 ).T @ dz2_dw1
        dc_dw2 = (dj_da3 * da3_dz3).T @ dz3_dw2

        return dc_dw1, dc_dw2

    def train(self, X, y):
        for i in range(self.n_iters):
            a1, z2, a2, z3, a3 = self.forward_propagate(X)
            y_matrix = np.eye(self.num_labels)[y.flatten()]
            cost = self.compute_cost(a3, y_matrix, X.shape[0])
            self.epochs += 1
            self.losses.append(cost)

            theta1_grad, theta2_grad = self.back_propagation(
                a1, z2, a2, z3, a3, y_matrix
            )
            self.theta1 -= self.alpha * theta1_grad
            self.theta2 -= self.alpha * theta2_grad

            # print(f'Epoch {self.epochs}, Cost: {cost}')

    def predict(self, X):
        _, *_, a3 = self.forward_propagate(X)
        return np.argmax(a3, axis=1)
    
    def restart(self):
        self.losses = []
        self.epochs = 0
        self.initialize_weights()
    