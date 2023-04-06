# Cybersecurity for IT Professionals

These are open educational resources ([OER](https://en.wikipedia.org/wiki/Open_educational_resources)) for IT professionals who want to get a better grasp of cybersecurity.
They are to be used by teachers, trainers, students and hobbyists who have an IT / CS (_Computer Science_) background.

## Using the Content

Content is located in the `content/` folder.
It consists of 10 chapters:

* [Security Principles and Terminology](content/chapters/security-principles/)
* [Account Management and Password](content/chapters/account-management/)
* [Access Control, Privileges, Isolation](content/chapters/access-control/)
* [Data Protection](content/chapters/data-protection/)
* [Runtime Application Security](content/chapters/runtime-security/)
* [Web Application Security](content/chapters/web-security/)
* [Network Monitoring and Defense](content/chapters/network-monitoring/)
* [Penetration Testing](content/chapters/penetration-testing/)
* [Security Audit](content/chapters/security-audit/)
* [Intrusion Detection and Intrusion Prevention](content/chapters/detection-prevention/)

Each chapter has its own folder.
Content for each chapter is split in two subfolders:
* `lecture/`: content to be presented and discussed as part of lectures / presentations
* `practice/`: content to be worked on as practical activities

Lecture content is expected to be presented and followed.
Practice content is expected to be used hands-on individually or as part of team.

## Chapter Contents

### Lecture

Lecture content consists of slides, demos, media files and quizzes in the `lecture/` subfolder of each chapter.

Slides are written in [GitHub Markdown](https://guides.github.com/features/mastering-markdown/) and use [reveal-md](https://github.com/webpro/reveal-md) and [reveal.js](https://revealjs.com/) to render HTML output.
Building slides requires [MarkdownPP](https://github.com/amyreese/markdown-pp).
Lecture slides are built from the `slides.mdpp` file using the `make` command (and the `Makefile`).
`slides.mdpp` is a wrapper / index file;
actual content is stored in Markdown format in files in the `slides/` subfolder.
Output is generated in the `_site/` subfolder;
open the `_site/index.html` in a browser to view the slides.

Demos are snippets of code and support files that showcase concepts and ideas related to the lecture.
Demos are located in the `demo/` subfolder.
Each demo has its own folder with source code, `Makefile` or other build files (if required) and support files.

Media files are images and films used in slides for visual support.
Media files are located in the `media/` subfolder.

Quizzes are used in slides to trigger interactivity with participants and as a form of (self-)assessment.
Quizzes are located in the `quiz/` subfolder.
Quiz questions are stored in [Markdown format](https://guides.github.com/features/mastering-markdown/), one file per quiz.

### Practice

Practice content consists of background text, media files, support files and quizzes in the `practice/` subfolder of each chapter.

Background text is located in `content/` folder as a series of sections.
Each section consists of general information, tutorial information followed by description of actual work items and a quiz.
Sections are indexed in the `README.md` file.

Support files for work items are stored in the `support/` subfolder.
There is a subfolder for each section.
Each section subfolder contains source code, `Makefile` (or other build files, if required) and support files.

Media files are images and films used in text for visual support.
Media files are located in the `media/` subfolder.

Quizzes are referenced at the end of each section as a form of (self-)assessment.
Quizzes are located in the `quiz/` subfolder.
Quiz questions are stored in [Markdown format](https://guides.github.com/features/mastering-markdown/), one file per quiz.

## Contributing

Contributions are welcome.
See the [contribution guide](CONTRIBUTING.md) on how you could report or fix issues and on how you can improve the content.

Reviewers are requested to follow the [reviewing guide](REVIEWING.md).
