## Course Context: COMP 395 – Deep Learning

**Course Overview:** This upper-division computer science course covers the theoretical foundations and practical applications of deep neural networks. Students learn the mathematics of backpropagation, optimization strategies, and modern architectures including CNNs (vision), RNNs/LSTMs (sequences), and Transformers (NLP and vision). The course emphasizes both rigorous mathematical understanding and hands-on implementation.

**Student Profile:** Primarily computer science majors with working knowledge of Python and calculus. Students are expected to be comfortable with partial derivatives, matrix operations, and debugging code. Some students may come from adjacent quantitative fields.

**Pedagogical Approach:** This course prioritizes deep understanding over rapid prototyping. Students must grasp the underlying mathematics (chain rule, gradients, loss landscapes) and be able to implement core algorithms from scratch before using high-level abstractions. AI tools may be used for boilerplate code (environment setup, data loading, plotting), but students must be able to explain and recreate the logic of any neural network code they submit.

**Learning Objectives:**
- Understand the mathematical basis of learning in neural networks
- Implement deep learning models using PyTorch (and sometimes raw NumPy)
- Diagnose and resolve common training issues (overfitting, vanishing gradients)
- Read and implement concepts from current research papers
- Consider ethical implications of large-scale AI deployment

**Assignment Types:**
- *Labs (24%):* Paired, guided exercises applying new concepts (e.g., building a perceptron, setting up training loops). Due end of day.
- *Homework (30%):* Individual implementation tasks requiring deeper engagement—often "from scratch" implementations alongside PyTorch versions
- *Projects (21%):* Larger builds (image classifiers, sentiment analysis tools). Individual or group work, individual submission.
- *Quizzes (12%):* Timed, individual programming assignments. Open book/internet, no communication.

**Submission & Tools:** Coding assignments are submitted via GitHub Classroom. Students use Python 3 and PyTorch. Proper commit practices expected.

**AI Policy:** AI/LLM use is permitted for boilerplate and debugging, but students must include a transcript of any AI conversation in their submission. Students must be able to verbally explain any code they submit—inability to do so is considered plagiarism.

**Note for Beamers and Latex:** When generating slides as Beamers, please make it so that code lines aren't in the slides involving code, as this makes it difficult for students to copy and paste the code. You need to add the upquote package to keep the quotes as straight ASCII quotes that copy correctly as well


**Note on Pedagogy**
Some activities need to be didactic, but generally the approach should be from a cognitivist ( metacognition, attention to forming schema) or constructivist ( students build knowledge together). In instructional slides there should be small activities where students think pair share about bigger ideas, or to discuss conceptual knowledge 

---

## Prior Assignments

**Assignment 0: GitHub Collaboration & Environment Setup**
Students learned to collaborate using GitHub (forking, cloning, branching, pull requests) and set up Python virtual environments for reproducible development workflows.

**Assignment 1 (Homework): Partial Derivatives and Gradients**
A pen-and-paper practice assignment building the calculus foundations for deep learning. Students computed single partial derivatives, found both partial derivatives of multivariable functions with geometric interpretation (e.g., elliptic paraboloid), assembled gradient vectors for functions of four variables using the chain rule, and interpreted gradient direction and magnitude in context.

**Lab 2: Gradient Descent from Scratch**
A paired lab where students implemented gradient descent in NumPy from scratch. Starting with a chain rule refresher, students translated the gradient descent update rule into Python, minimized f(x,y) = (x-3)^2 + 2(y-1)^2, implemented stopping conditions using gradient norm, visualized descent paths on contour plots, and experimented with different learning rates and starting points.

**Assignment 4 (Lab): Binary Classification -- Breast Cancer**
Students implemented a from-scratch binary classifier (logistic regression) using PyTorch tensors on the sklearn breast cancer dataset. They built sigmoid, forward pass, MSE loss, and gradient functions by hand from derived equations, wrote a full training loop with per-sample gradient updates, normalized features using training-set statistics only, evaluated train/test accuracy, and visualized loss curves and learned feature weights. Includes think-pair-share activities on data leakage and model interpretability.

---

## Skills Learned Thus Far

- **Git & GitHub:** Cloning repos, branching, committing, pull requests, GitHub Classroom submission workflow
- **Python environments:** Creating and managing virtual environments for project isolation
- **Calculus for DL:** Partial derivatives, chain rule (single and multivariable), gradient vectors, geometric interpretation of gradients
- **Gradient descent:** The optimization algorithm, learning rate, convergence/stopping conditions, effect of hyperparameters on training behavior
- **NumPy fundamentals:** Array operations, `np.linalg.norm`, `np.linspace`, `np.meshgrid`
- **PyTorch basics:** Tensors, `torch.exp`, `torch.dot`, `torch.zeros`, converting between NumPy and PyTorch
- **From-scratch implementation:** Translating mathematical equations into working code without high-level abstractions
- **Data handling:** Train/test splits, feature normalization (and why to use only training statistics), loading sklearn datasets
- **Visualization:** Contour plots, loss curves, feature importance bar charts using matplotlib
- **Binary classification pipeline:** Forward pass, loss computation, backpropagation (manual gradients), weight updates, accuracy evaluation
- **ML concepts:** Sigmoid activation, decision boundaries, overfitting vs. underfitting intuition, hyperparameter experimentation

---

## Assignment Request

[Describe the specific assignment you need here—include the week/topic, type (lab, homework, project), relevant mathematical concepts,, how it relates to course goals overall, and whether you want "from scratch" implementation, PyTorch implementation, or both. Engage me in questioning if I leave any of this information out]