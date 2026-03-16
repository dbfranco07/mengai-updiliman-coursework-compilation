# Master of Engineering in Artificial Intelligence - UP Diliman Coursework Compilation

Hello! Welcome to this repository where I share my personal experiences, opinions, and outputs for the Master of Engineering in Artificial Intelligence program of the University of the Philippines Diliman.

## Table of Contents
- [Background](#background)
- [Core Courses](#core-courses)
  - [AI 201 - Fundamentals of Artificial Intelligence](#ai-201---fundamentals-of-artificial-intelligence)
  - [AI 211 - Computational Linear Algebra for AI](#ai-211---computational-linear-algebra-for-ai)
  - [AI 212 - Probability and Statistics for AI](#ai-212---probability-and-statistics-for-ai)
  - [AI 221 - Classical Machine Learning](#ai-221---classical-machine-learning)
  - [AI 222 - Advanced Machine Learning](#ai-222---advanced-machine-learning)
  - [AI 231 - Machine Learning Operations](#ai-231---machine-learning-operations)
- [Foundational and Elective Courses](#foundational-and-elective-courses)
  - [ES 204 - Numerical Methods for Engineering](#es-204---numerical-methods-for-engineering)
  - [IE 211 - Quantitative Methods for Engineering](#ie-211---quantitative-methods-for-engineering)
  - [AI 361 - Autonomous Robots](#ai-361---autonomous-robots)
  - [CS 282 - Computer Vision](#cs-282---computer-vision)
- [Disclaimer](#disclaimer)
- [License](#license)
- [Star](#star)


## Background

Just to share some context with everyone: my undergraduate background is in Aeronautical Engineering, and I had never written any production-level code before this. Prior to enrolling in the program, my experience with AI and machine learning was very minimal—essentially negligible. However, as I’ve progressed through the different courses and collaborated with my fellow students, I have been able to gain invaluable knowledge relevant to the development of AI.

## Core Courses

The courses below are those required by the program to take. While it is advised to take them in order based on the course code, it is not a necessary.

### AI 201 - Fundamentals of Artificial Intelligence

This course (the name of which can be quite deceiving) is considered by many to be the "weeder course" of the AI program, as a large percentage of students drop out mid-semester. The curriculum provides a significant level of depth, helping students understand the various branches under the umbrella of Artificial Intelligence. While a large chunk of the course is dedicated to introducing machine learning, it also tackles topics outside that scope, such as search methods and constraint satisfaction.

The bulk of the course involves implementing methods from scratch through programming assignments, a few exams, and a mini-project. The assignments are difficult because we have to implement machine learning algorithms, such as a multilayer perceptron, using only `NumPy`! Each assignment usually takes me a week or two to code, and we also need to document the results using a conference-level LaTeX paper template. I’m not going to lie, though, getting it all to work without using popular Python libraries like PyTorch or TensorFlow is so satisfying! Of course, the training process took a long time since it was written solely in NumPy without any GPU or AI accelerators involved. :(

The exams here are also very difficult. One of the most memorable parts of the exam was when we were asked to derive the backpropagation algorithm. Our professor always emphasizes that this is one of the most important things that we must know by heart as an AI student. This ensures that "AI" is not just a buzzword to us, but is something that we actually understand at a granular level.

I would say this is one of those courses that truly tests how much you want to be in this program. As our professor always likes to say: "If the tough gets going, the going gets tough." 


**Topics covered:**

- Basic Computer Science Concepts and introduction to machine learning.


**Programming Assignments:**  
Note: I did not get perfect scores here. I had a few mistakes on each assignment (maybe around 5-10 deducted points) so read with a grain of salt.
- Programming Assignment 1 - Implementing the A* Algorithm
  - [Code](AI-201/notebooks/a_star_implementation.ipynb)
- Programming Assignment 2 - Naive Bayes Spam Filter
  - [Code](AI-201/noteooks/naive_bayes_spam_filter.ipynb)
  - [Paper](AI-201/papers/PA2_Report.pdf)
- Programming Assignment 3 - Implementing the Backpropagation Algorithm
  - [Code 1](AI-201/notebooks/neural-network-class.ipynb)
  - [Code 2](AI-201/notebooks/generate-balanced-data-using-SMOTE.ipynb)
  - [Paper](AI-201/papers/PA3_Report.pdf)
- Programming Assignment 4 - Comparison of Boosted Perceptrons and SVM
  - [Code](AI-201/notebooks/boosted_perceptrons_and_svm.ipynb)
  - [Paper](AI-201/papers/PA4_Report.pdf)
- Mini-Project - Optimizing Classification Capability of Classical Machine Learning Models on Traffic Signs
  - [Code](AI-201/notebooks/traffic-signs.ipynb)
  - [Paper](AI-201/papers/Optimizing%20Classification%20Capability%20of%20Classical%20Machine%20Learning%20Models%20on%20Traffic%20Signs.pdf)
  - [Slides](AI-201/slides/Optimizing%20Classification%20Capability%20of%20Classical%20Machine.pptx)


---

### AI 211 - Computational Linear Algebra for AI

This course was actually the very first one I took (alongside IE 211). In high school, I had a linear algebra course, and during my undergrad, I took Advanced Engineering Mathematics, which involved matrix problems, but AI 211 was a different breed! We weren't only expected to perform matrix operations by hand, but we also had to be able to implement them efficiently in code.

Most of our grades came from handwritten exams, problem sets, and journals. I actually liked the journal part; after every discussion, we needed to reflect on what we had learned and our thought process regarding the lesson. We could also include any confusion or questions we had in the journal. The exams were also difficult since most of the questions involved essays. One question I vaguely remember asked us to compare two methods and identify which was more efficient for a specific problem.

The problem sets were also difficult but actually fun. They required us to write code and then document it as well. Each problem set involved about 4–5 problems, and each one required significant effort. Similar to AI 201, the problem sets were challenging because they required us to write ML algorithms using linear algebra techniques.

**Topics covered:**

-  Matrix operations, matrix decompositions, vector calculus, applications in machine learning, etc.

**Problem Set:**

- [Notebook](AI-211/AI211_probset.ipynb)
- [Source Code](AI-211/ai211.py)
- [Documentation](AI-211/AI211%20Problem%20Set%20Documentation.pdf)

---

### AI 212 - Probability and Statistics for AI

While I believe most of us have already taken a statistics course at some point during our undergraduate programs, this class made me doubt if I ever really understood any of it before. The first half of the semester focused on probability and building a solid foundation, while the second half was dedicated to statistics and how it connects to AI and machine learning.

For me, this has been the most difficult course so far in terms of theory. I think it was during the first week that the concept of sigma-algebra was introduced, and it has stuck with me ever since as something incredibly abstract. While our professor explained it well, it was something my brain stubbornly resisted truly grasping. Also, I remember having to perform the integration of a beta function; something I had never done before!

The course involved two exams, two batches of problem sets, quizzes, and journals. A saving grace was that the problem sets were group-based, which allowed me to collaborate with my teammates. If I remember correctly, I actually failed the first exam, so I really struggled to figure out how to make a comeback.

The approach of this course is genuinely demanding. While it provides a vital foundation for understanding machine learning, I honestly had a hard time. I’m not sure if that was because I was also taking AI 201 and ES 204 that semester—a total of 9 units—and I ended up "sacrificing" this course since I also have a full-time job. Nonetheless, passing this class felt truly fulfilling.


**Topics covered:**

- Probability, random variables, density and mass functions, statistical inference, bayesian inference, markov chain monte carlo, etc.

**Problem Set:**

- TBA

---

### AI 221 - Classical Machine Learning

When I was taking this class, I wasn't enrolled in any other courses (aside from my full-time job, of course), so I was able to spend more time on it compared to the others. This was also the first course I took that didn't have any long exams or quizzes. Our grades relied purely on machine exercises (though we had one every week), a final project, and a paper review. Because of this, I didn't need to spend time memorizing a lot of information overnight—yup, I do tend to cram, lol—I just needed to implement the lessons using code and actual data.

While implementing machine learning algorithms was nothing new, this was the first time we were allowed to use programming libraries (especially `Scikit-Learn`) other than bare-bones `NumPy`. Gosh, that was such a relief! It made the training part much more efficient since (1) `Scikit-Learn` is already robustly tested for efficiency, and (2) we didn't need to prototype the training code from scratch; we just needed to call the .fit() method.

The way the class worked was that we would study a certain algorithm (or group of algorithms), apply them to data provided by our professor, and then evaluate the results. The goal was to familiarize ourselves with different models and experiment with them. Of course, we also tackled necessary techniques like train-test splitting, cross-validation, hyperparameter tuning, and watching out for signs of overfitting. At the end of the semester, the final project was to find our own data and perform machine learning experiments on it using everything we had learned in the course.

**Topics covered:**

- Exploratory data analysis and different machine learning algorithms such as linear models, SVM, MLP, tree-based models, ensemble methods, and explainability.

**Machine Exercises:**

- TBA

---

### AI 222 - Advanced Machine Learning

This was the course I found to be the hardest. Previously, it was called the "Deep Learning" class, but due to the fast-paced nature of AI research, our professor renamed it "Advanced Machine Learning" to cover topics outside the deep learning spectrum. We still deeply explored MLPs, CNNs, RNNs, and Transformers, but we also discussed topics such as generative models (e.g. GANs, VAEs, Flow Matching, Diffusion models, etc.), LLMs, and AI agents. Essentially, we tried to cover most of the state-of-the-art topics. Our professor even shared that he created his own agent framework since modern frameworks such as LangChain do not meet his intended requirements. I think that really sounds so cool!

The course was designed to be purely theoretical; we didn't have anything to code. The programming side was handled in the AI 231 course, which was taught by the same professor. In fact, it’s an unwritten rule that AI 222 and AI 231 are "corequisites" and should be taken in the same semester. AI 222 provides the theory, while AI 231 handles the application.

Don't let the theoretical design of the course lead you to believe it’s easy. In fact, that's exactly what made it so difficult. Our grades were based exclusively on three long exams and a small percentage for attendance (I think attendance was around 5%). A handful of students actually failed due to the difficulty! I was quite anxious after my first exam score was only a 69/100, lol. Thankfully, I scored 95/100 on the next one, which allowed me to breathe much more easily. However, I failed the last exam with a 55/100 because I got somewhat confused. Nonetheless, I was happy just to pass the course.

You might wonder what made the exams so difficult. Our professor designed them to be intentionally confusing to test if we truly understood the concepts or if we were just memorizing the lessons and "overfitting." Overall, it was a fun course and the one that really brought me in sync with the current state of Artificial Intelligence.

**Topics covered:**

- MLP, CNN, RNN, Transformers, detection and segmentation, generative models, LLM, AI agents, etc.

**Outputs:**

- None. Only 3 VERY difficult exams.

---

### AI 231 - Machine Learning Operations

This course tackles the same material taught in AI 222 but focuses heavily on the coding side. The main framework suggested to us was `PyTorch` for training. Our professor actually authored a book using `TensorFlow` and `Keras`, but he mentioned that nowadays they are too "painful" to use and he prefers to stick to `PyTorch`.

This class was a complete 180 from AI 222; there were no exams at all, only machine exercises. The first few exercises were easy enough that we could complete them quite quickly. They involved using tools like `einsum` and `einops` for their elegance, implementing `AlexNet` using only `NumPy`, learning how to use pretrained models, and training `YOLO` models using our own custom datasets.

The next few exercises shifted our focus to edge devices, specifically the Jetson Orin Nano. What made it more challenging was that we had to go to campus to develop since we couldn't bring the Jetsons home. We learned how to flash and boot the devices, write our own services, and—the juiciest part of the course—create a Point of Sale (POS) system using our trained `YOLO` model, running solely on the Jetson Orin Nano. This system uses the `YOLO` model to identify grocery items and register them properly. It’s essentially what you see in modern grocery stores, except it uses computer vision instead of barcodes.

The main challenge was ensuring the system's accuracy and efficiency. A delay in inference meant losing points, and an inaccurate prediction also resulted in point deductions. On top of that, we had to create a web UI (though honestly, thanks to modern AI like ChatGPT for helping with that part!). Our professor even encouraged us to use AI as an assistant, as long as we made sure to understand the code and didn't just accept everything blindly.

**Topics covered:**

- Coding tools, frameworks, and libraries, deployment, model serving, etc.

**Machine Exercises**

- TBA

---

## Foundational and Elective Courses

While every MEng AI student takes the same required core courses, the foundational and elective subjects can vary. In my case, I chose IE 211 and ES 204 as my foundational courses, and AI 361 and CS 282 as my electives. Although AI 361 is actually a core course for PhD students, my adviser allowed me to take it as an elective.

### ES 204 - Numerical Methods for Engineering

*Description placeholder*

**Topics covered:**

- Topic 1
- Topic 2

**Notebooks / Outputs:**

- TBD

---

### IE 211 - Quantitative Methods for Engineering

*Description placeholder*

**Topics covered:**

- Topic 1
- Topic 2

**Notebooks / Outputs:**

- TBD

---

### AI 361 - Autonomous Robots

*Description placeholder — Ongoing*

**Topics covered:**

- Topic 1
- Topic 2

**Notebooks / Outputs:**

- TBD

---

### CS 282 - Computer Vision

*Description placeholder — Ongoing*

**Topics covered:**

- Topic 1
- Topic 2

**Notebooks / Outputs:**

- TBD

---

## Disclaimer

> **Academic Integrity Notice:** The materials in this repository are shared for educational and reference purposes only. Please do **not** copy, reproduce, or submit any of these outputs as your own work. Doing so may violate your institution's academic integrity policies.
>
> **Accuracy Notice:** The outputs, solutions, and opinions shared here are my own and may contain errors or inaccuracies. They should not be treated as authoritative or definitive answers. Always verify with official course materials and consult your instructors.
>
> **Opinions Disclaimer:** All views, opinions, and commentary expressed in this repository are solely my own and do not represent or reflect the views of my professors, the College of Engineering, or the University of the Philippines Diliman.

## License

This repository is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).

You may view and reference this work, but you may not copy, redistribute, or create derivative works from it for commercial or academic submission purposes.


## Star

If you liked or enjoyed reading my experiences, feel free to leave a star. It will be highly appreaciated! :)