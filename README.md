# InternMatch: A Collective Intelligence Internship Recommendation System

## 1. Goal of the Project
The primary goal of this project is to develop a Collective Intelligence Internship
Recommendation System that addresses the existing challenges in the internship placement
process at UM6P. By leveraging the power of advanced technologies, such as openAI's DaVinci
and Ada Models, the system aims to intelligently match students' preferences with companies'
internship opportunities.

## 2. Problem Statement
In today's rapidly evolving job market, internships have become an integral part of students'
academic and professional journey (Zopiatis, et al., 2021). These valuable opportunities provide
students with hands-on experience, exposure to real-world challenges, and a chance to apply
their theoretical knowledge in practical settings. However, the process of matching students
with suitable internship positions can be challenging, especially when considering their
individual preferences and the specific needs of companies offering internships (Adeosun et al.,
2022).

At UM6P, we currently lack a robust recommendation system that takes into account students'
preferences and feedback when matching them with internship positions. As a result, the
current placement process may not fully optimize the potential for students to secure
internships that align with their interests and career goals. Additionally, companies may
struggle to find interns who possess the specific skills and qualities they seek, leading to
suboptimal outcomes for both parties involved.

## 3. Importance of the Project
The implementation of an effective internship recommendation system holds significant
importance for UM6P and its students. Internships serve as a bridge between academia and
industry, allowing students to acquire practical skills, build professional networks, and explore
potential career paths. By facilitating successful internships that align with students'
preferences, UM6P can greatly enhance the professional development and employability of its
students.

Furthermore, an efficient recommendation system has the potential to strengthen UM6P's
reputation and foster fruitful partnerships with companies. When students are well-matched
with internships that suit their interests and skills, they are more likely to perform exceptionally
well during their internships (Cappelli, 2012). This not only benefits the students themselves
but also enhances the reputation of UM6P as a provider of high-quality education and talented
graduates. As a result, UM6P can attract new partnerships with companies that are aligned with
students' preferences and contribute to the overall growth and success of the institution.

## 4. Approach
The Collective Intelligence Internship Recommendation System was designed as a web-based
platform that allows students to interact and provide their preferences in the form of job roles,
work culture, and location of companies they wish to do internship with. The approach was
developed in three stages.

### 5. Utilizing OpenAI Tools (DaVinci, Ada Models)
To enhance the recommendation system's capabilities, we leveraged OpenAI tools, specifically
the DaVinci (text completion) and Ada (embedding generation) Models. These powerful large
language models enabled the platform to analyze and process textual data efficiently, extract
relevant information from students' preferences and companies' needs, and generate embedding
for both the user's input and the backend datastore, which was now used in the second stage of
the process.

### 5.1. Utilizing Geopy
Geopy is a Python library that provides various geocoding and geolocation functionalities. It
allows developers to easily retrieve geographical information such as coordinates, addresses,
and distances between locations. This was used in the the Collective Intelligence Internship
Recommendation System to convert the users input location into coordinates (latitude and
longitude), which permitted the computation of distance between the users preferred location
for internship and that of the companies.

### 5.2. Similarity Computation
Cosine similarity is a technique that measures the similarity between two vectors based on the
angle between them. In the context of the internship recommendation system, cosine similarity
was computed to assess the compatibility between a student's preferences vector and the vector
of internship positions available in the server's datastore. By calculating the cosine similarity
score, the platform was able to determine the degree of similarity and prioritize relevant
company recommendations and this was saved to a user's matrix. The similarity computation
was done using the metrics pairwise module of sklearn.

### 5.3. Collective Intelligence Tools and Application
The system leverages collective intelligence techniques in order to improve its accuracy and
effectiveness. The description below is how collective intelligence was used to continuously
refine the recommendation algorithm, based on the wisdom of the crowd to generate more
accurate recommendations.

#### 5.3.1. Pareto Front Analysis
The method of Pareto Front Analysis was used on the user’s matrix to identify the optimal
solutions (a short list of companies displayed as recommendation) from the entire companies
dataset. This was done by identifying the companies that are not dominated with regard to the
criteria (role description, work culture and location).
A company A is said to be dominated if there exists one other company B that:

● Performs better than company A in at least one criterion

and

● Performs at least as well as company A in all other criteria

#### 5.3.2. Feedback Mechanism and Platform Rating
The system has a feedback mechanism that helps users to review their experiences. A rating
feature is also implemented, allowing users to rate the overall performance and usefulness of
the system. By collecting feedback and ratings, the system can learn from past experiences and
make better recommendations in the future. This is where an iterative development can become
very useful given that the development team can address any issues or concerns raised by users.

#### 5.3.3. Iterative Improvement
Iterative improvement is a fundamental aspect of our project. The goal is to enhance the
recommendation system continuously. The feedback mechanism, added to the platform, helps
to collect reviews and ratings from users. This is to identify areas for improvement. The
analysis of these feedback will provide insights that can be used to

● Refine the recommendation algorithm,

● Update preferences (by removing or adding some new criteria),

● Optimize the matching process,

● Update companies’ dataset.

This iterative development approach ensures that the system evolves and becomes more
accurate over time.
