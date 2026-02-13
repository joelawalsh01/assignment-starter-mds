## Course Context: COMP 395 – AI and Learning Technologies

**Course Overview:** This upper-division computer science course bridges educational theory and artificial intelligence. Students explore learning theories (behaviorism, cognitivism, constructivism, constructionism) and their implications for designing computer-assisted learning technologies—from early teaching machines to modern Intelligent Tutoring Systems and Generative AI.

**Student Profile:** Primarily computer science majors, with some students from other disciplines (education, cognitive science, etc.). Students have working knowledge of Python and version control (GitHub). Multidisciplinary teams collaborate throughout the course.

**Pedagogical Approach:** A significant component of the course teaches systems design, infrastructure, and how web applications work through "vibecoding"—rapid, AI-assisted prototyping where students learn by building. Students use tools like Figma, Streamlit, and Claude Code to quickly iterate on ideas while developing practical understanding of REST APIs, frontend technologies (HTML/CSS/JS), and deployment pipelines (CI/CD).

**Learning Objectives:**
- Analyze educational tools through major learning theories
- Critique the history of teaching machines and recurring ed-tech pitfalls
- Design, prototype, and evaluate AI-driven learning technologies
- Evaluate ethical implications (data privacy, algorithmic bias)
- Develop practical skills in web app architecture and rapid prototyping

**Assignment Types:**
- *Labs/Studios (20%):* Hands-on exercises applying concepts—both theoretical (designing reinforcement schedules) and technical (building prototypes, working with APIs)
- *Individual Assignments (15%):* Theoretical analysis of existing tools or reading reflections
- *Projects (47%):* Team-based design, prototyping, and evaluation of novel learning technologies

**Submission & Tools:** Coding assignments are submitted via GitHub Classroom. Students are expected to use proper commit practices and may have CI/CD pipelines for automated testing.

**AI Policy:** Students may use AI tools but must disclose use, include a "prompts appendix," and explain the reasoning behind AI-generated decisions.


**Note for Beamers and Latex:** When generating slides as Beamers, please make it so that code lines aren't in the slides involving code, as this makes it difficult for students to copy and paste the code. You need to add the upquote package to keep the quotes as straight ASCII quotes that copy correctly as well

**Note on Pedagogy**
Some activities need to be didactic, but generally the approach should be from a cognitivist ( metacognition, attention to forming schema) or constructivist ( students build knowledge together). In instructional slides there should be small activities where students think pair share about bigger ideas, or to discuss conceptual knowledge 

---

## Assignments Completed So Far

**Reading: Skinner's "Teaching Machines" (1958)**
Students read B.F. Skinner's foundational paper on programmed instruction. The reading introduced key behaviorist principles: small steps, active responding, immediate feedback, self-pacing, and low error rates. This provided the theoretical backdrop for later lab work.

**Lab 1: Wordcloud Analysis (Week 1)**
Students created wordcloud visualizations in a Jupyter notebook using Python. This served as a warmup to reactivate Python skills and introduce the notebook-based workflow used in the course.

**Lab 2: Collaborative Development with Git & CI/CD Workflows (Week 2)**
Teams of 2-3 practiced the feature branch workflow on a shared GitHub repository. Each student created a feature branch, implemented a feature (e.g., bar charts, word frequency stats), opened a pull request with a meaningful description, conducted peer code review, and merged to main. Extension: converting a notebook to a CLI script with pytest tests.

**Lab 3a: Introduction to APIs and Flask (Week 3)**
Students set up a conda virtual environment, installed Flask and requests, and built a minimal Flask application with two endpoints (`/` and `/greet`). They also wrote a Python client script using the `requests` library to communicate with their own API. Covered the distinction between building and consuming APIs.

**Lab 3b: Building a Skinner Teaching Machine in Flask (Week 3)**
Students designed and built a web-based teaching machine implementing Skinner's programmed instruction principles. They created a frame data structure (Python dicts), wrote 5-10 instructional frames on a topic of their choice, implemented Flask routes (`/`, `/frame`, `/submit`, `/complete`), built Jinja2 HTML templates, and used Flask sessions to track progress and score. Extension options included hints, multiple accepted answers, branching frames, and timing data. Included reflection questions connecting the build experience back to learning theory (Skinner vs. Papert/constructionism).

---

## Skills Acquired So Far

**Python & Data Science**
- Python fundamentals (dicts, lists, string manipulation, f-strings)
- Jupyter notebooks for exploratory analysis
- Data visualization with wordcloud and matplotlib

**Version Control & Collaboration**
- Git basics: clone, branch, add, commit, push, pull
- Feature branch workflow (create branch, develop, PR, review, merge, delete)
- Writing meaningful commit messages and PR descriptions
- Peer code review on GitHub
- Resolving merge conflicts

**Environment Management**
- Creating and activating conda virtual environments
- Managing dependencies with `requirements.txt` and `pip install`
- Isolating project dependencies across different projects

**Web Development (Flask)**
- Flask application structure: routes, decorators, request handling
- HTTP fundamentals: GET/POST requests, query parameters, form data
- Jinja2 templating: template inheritance, variables, conditionals
- Flask sessions for maintaining state across requests
- Client-server architecture: building APIs and writing client scripts
- Project structure: separating data (frames.py), logic (app.py), and presentation (templates/)

**Learning Theory**
- Behaviorism: Skinner's programmed instruction principles (small steps, active response, immediate feedback, self-pacing)
- Connecting theory to practice: designing instructional frames that embody behaviorist principles
- Beginning to critique behaviorist approaches through the lens of constructionism (Papert)

**Software Engineering Practices**
- CI/CD concepts and workflow
- Code review as a collaborative practice
- Writing automated tests with pytest
- Structuring projects with separation of concerns

---

## Assignment Request

[Describe the specific assignment you need here—include the week/topic, type (lab, homework, project), relevant mathematical concepts, how it relates to course goals overall, where you want think pair shares inserted, and whether you want "from scratch" implementation, etc. Engage me in questioning if I leave any of this information out]

