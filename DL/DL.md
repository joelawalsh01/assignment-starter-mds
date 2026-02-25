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

**Critique each lesson like a learning scientist would**
Use this critique to stregthen the lesson. Ensure that there is (whenever possible) activities that access and build on prior knowledge, appropriately scaffold, give opportunities for metacognition, allow for students to refine schema, and formatively assess learning. 

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

**Lab 4: From Linear Models to Multilayer Perceptrons (2-day lab)**
*Day 1 (Theory):* Beamer lecture building from the linear classifier in Assignment 4 to MLPs. Students explored why linear models produce flat (hyperplane) decision boundaries, proved that stacking linear layers without activation collapses to a single linear layer, and learned that nonlinear activations (ReLU) between layers are the essential ingredient that makes depth meaningful. Covered ReLU vs. sigmoid for hidden layers (vanishing gradient problem), BCE loss vs. MSE for classification (stronger gradients for confident wrong predictions), and backpropagation as the chain rule applied layer-by-layer right to left. Includes TensorFlow Playground exploration and a pen-and-paper forward/backward pass exercise on a tiny 2-input, 2-hidden, 1-output network.
*Day 2 (Implementation):* Paired Jupyter notebook lab on the UCI Sonar dataset (208 samples, 60 frequency-band features, mines vs. rocks). Students built a linear classifier baseline using `nn.Module`, wrote a reusable training function with BCE loss and Adam optimizer, then designed and trained their own MLP architectures. Ran at least 5 architecture experiments varying depth, width, and activation functions, all logged to MLflow. Visualized PCA-projected decision boundaries comparing linear vs. MLP models. Compared best MLP against a Random Forest baseline to discuss when neural networks are the right tool vs. simpler methods on small tabular data. Pulled MLflow experiment data into pandas and wrote a research-backed analysis report.

---

## Skills Learned Thus Far

- **Git & GitHub:** Cloning repos, branching, committing, pull requests, GitHub Classroom submission workflow
- **Python environments:** Creating and managing virtual environments for project isolation
- **Calculus for DL:** Partial derivatives, chain rule (single and multivariable), gradient vectors, geometric interpretation of gradients
- **Gradient descent:** The optimization algorithm, learning rate, convergence/stopping conditions, effect of hyperparameters on training behavior
- **NumPy fundamentals:** Array operations, `np.linalg.norm`, `np.linspace`, `np.meshgrid`
- **PyTorch basics:** Tensors, `torch.exp`, `torch.dot`, `torch.zeros`, converting between NumPy and PyTorch
- **PyTorch `nn.Module`:** Defining models as classes with `__init__` and `forward`, `nn.Linear`, `nn.ReLU`, `nn.Sigmoid`, `nn.Sequential`; using `model.parameters()`, `model.train()`, `model.eval()`
- **Autograd and optimizers:** `loss.backward()` for automatic gradient computation, `optimizer.zero_grad()` / `optimizer.step()` pattern, Adam optimizer, `torch.no_grad()` context for evaluation
- **Loss functions:** MSE loss (from-scratch and `nn.BCELoss`); understanding why BCE gives stronger gradients than MSE for classification (gradient analysis for confident wrong predictions)
- **From-scratch implementation:** Translating mathematical equations into working code without high-level abstractions
- **Data handling:** Train/test splits, feature normalization (and why to use only training statistics), loading sklearn datasets, `StandardScaler`, `stratify` parameter
- **Visualization:** Contour plots, loss curves, feature importance bar charts, PCA-projected decision boundary plots using matplotlib
- **Binary classification pipeline:** Forward pass, loss computation, backpropagation (manual gradients), weight updates, accuracy evaluation
- **MLP architecture:** Designing multi-layer perceptrons, choosing depth/width/activation functions, understanding why stacking linear layers without activation collapses to one layer
- **Activation functions:** ReLU for hidden layers (gradient is 0 or 1, no vanishing), sigmoid for binary output; understanding the vanishing gradient problem with sigmoid in hidden layers
- **Backpropagation theory:** Forward pass then backward pass, chain rule applied layer-by-layer, upstream gradient times local derivative pattern, hand-computing gradients through a small network
- **Experiment tracking:** MLflow (`set_experiment`, `start_run`, `log_param`, `log_metric`, `log_model`, `search_runs`); systematic architecture comparison with logged hyperparameters and metrics
- **Dimensionality reduction:** PCA for visualization (`PCA`, `fit_transform`, `inverse_transform`, variance explained)
- **Model comparison:** Linear vs. nonlinear classifiers, neural networks vs. tree-based methods (Random Forest) on small tabular datasets; understanding when each approach is appropriate
- **ML concepts:** Sigmoid activation, decision boundaries (linear vs. nonlinear), overfitting vs. underfitting intuition, hyperparameter experimentation, linearly vs. non-linearly separable data, model capacity vs. dataset size tradeoffs

---

## Assignment Request

[Describe the specific assignment you need here—include the week/topic, type (lab, homework, project), relevant mathematical concepts,, how it relates to course goals overall, and whether you want "from scratch" implementation, PyTorch implementation, or both. Engage me in questioning if I leave any of this information out]