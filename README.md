Demystifying Early Test Termination Due to Assertion Failure::


Step by step guidelines for using our dataset:
1.	There are 6 projects in this repository. One can find here math, jackson-core, joda-time, jfreechart, lang, and fastjson. 
2.	In the individual project directory, there are three different settings (original, error-collector, slicing) depending on our experiment. Anyone can easily find all of our experimental changes into these three settings. Moreover, coverage information is found into the target directory of every project.
3.	One can run every project from any directories using Maven dependencies and Junit plugin. We have used java version-8 for three projects (lang, math, and time) and rest others projects java version-11 is used. To run a project use below commands:
	mvn clean;
	mvn build;
	mvn compile;
	mvn test;
	To get the coverage report use the following command:
	mvn jacoco:report
4.	Finally, we have used open-source FLACOCO project for getting suspiciousness score and rank of buggy lines. FLACOCO generated reports (.CSV file) is found in every project folder according to their three settings.
5.	Scrips are written to calculate evaluation metrics, assertions count, finding multiple assertions, and get specific test failure report.
