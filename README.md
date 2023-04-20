# capstone-dekalbda-covidpolicy
Materials for the Emory QTM COVID policy capstone project in partnership with the Office of the DeKalb District Attorney
![Logo](/image/QTM_Logo.png)

## Contents
- [Motivation](#motivation)
- [Partners of Project](#partners-of-project)
- [Intended Use of Project](#intended-use-of-project)
- [Setup](#setup)
- [Notebook](#notebook)
- [Acknowledgements](#acknowledgements)

# Motivation
This project describes the process undergone to analyze the Office of the DeKalb County District Attorney’s (ODDA) Policy Regarding Case Backlog Due to the COVID-19 Pandemic. The policy expanded the criteria for non-violent felonies eligible for dismissal and pretrial diversion to include certain drug, forgery, theft, financial crime and burglary charges. Using data sets provided by the ODDA, outside recidivism data from Vera Incarceration Trends and demographic data from the American Community Survey from the United States Census Bureau, we analyzed how the policy impacted the DeKalb County community as it pertains to Prosecutorial Performance Indicators and best-practice recidivist metrics, specifically the recidivism rate within DeKalb county and the severity of recidivist crimes. In particular, we focus on case processing efficiency, re-offender information and potential demographic disparities. The results will be helpful for identifying any weaknesses or strengths present in the policy guidelines and inform any future decisions concerning its continuance or termination.
# Partners of Project
We collaborated with [Office of the DeKalb County District Attorney](https://www.dekalbda.org/) for this project. Office of the DeKalb County District Attorney is the prosecutor agency representing Georgia State in Stone Mountain Judicial Circuit.

For this project, Office of the DeKalb County District Attorney has provided us guidelines, legal aid, prosecution-related data from the DeKalb District Attorney jurisdiction, and feedback to our analysis to account for an accurate representation of impact of the ODDA's Policy Regarding Case Backlog Due to the COVID-19 Pandemic. 
# Intended Use of Project
A typical user of this Github repository should have interest in the following:
- learn the recidivism of the convicted through data from DeKalb County District Attorney’s jurisdiction
- understand how to apply satistical inference in recidivism analysis
- explore the impact of government intervention on recidivism

This repository is designed to help Python and R users to analyze and visualize the recidivism in DeKalb County District Attorney’s jurisdiction.
## Use of Data Sources
The data used in this project is provided and permitted by Office of the DeKalb County District Attorney, which shall not be displayed on any public device and space and shall not remain on any personal computer after the project is finished. Therefore, this Github repository will not display or store the data.
# Setup
This section instructs the user how to prepare necessary tools and environment for replicate our research.
## Installation
### Python
Go to the official [Python download page for Windows](https://www.python.org/downloads/windows/).

Find a stable Python 3 release. Any python version >=3.9.0 will satisfy the code written for the project.

Click the appropriate link for your system to download the executable file: Windows installer (64-bit) or Windows installer (32-bit).
![img2](/image/python_release.png)

Follow the default setting and finish the installation
![img3](/image/python_finish.png)

You can verify whether the Python installation is successful either through the command line or through the Integrated Development Environment (IDLE) application, if you chose to install it.

Go to Start and enter cmd in the search bar. Click Command Prompt.

Enter the following command in the command prompt:

python --version

An example of the output is:

Output
Python 3.10.10

### Pycharm
You can download PyCharm from the [JetBrains website](https://www.jetbrains.com/pycharm/).

Choose Community Edition which will be enough for the project.

Follow the default setting and finish the installation.

![download-pycharm.jpg](image%2Fdownload-pycharm.jpg)

### Anaconda

Visit [Anaconda.com/downloads](https://www.anaconda.com/download/)

Select Windows

Download the .exe installer

Open and run the .exe installer with the default setting

Search Anaconda in the search bar

Click Anaconda Navigator (Anaconda 3)

![download-pycharm.jpg](image%2Fdownload-pycharm.jpg)

Open Jupyter Notebook

![jupyter.png](image%2Fjupyter.png)

Find the .ipynd file of the project and finished

### Install prerequisite Python packages

Open pycharm and open the command line, input:

> pip install numpy pandas

## Dataset
The dataset used in this Capstone project can not be uploaded to public repository and are not allowed to be stored on any personal or public device without the permission from the DeKalb District Attorney Office. However, in the readme, the structure of the data and explanation of variables used will be included.

# Code
In our capstone project, we have one notebook. finalNotebook.ipynb notebook is a integrated notebook used both data cleaning, analysis, and visualization. We extract useful factors and target variables from raw datasets and combine them into cleaned datasets. Then we produce visualization to important factors that stakeholders care about, mainly recidivism-related variables. 

- Decision Making Method: The decision-making method used in this study will be based on Z-test significance testing, which will help to identify the effect of the policy on recidivism rates and therefore community safety, and a structural break, which identifies points in time during which noticeable changes in case management efficiency occurred.


- Policy Eligibility Criteria: A bank containing all the statutes associated with charges flagged as policy eligible by a prosecutor was created. Defendants were considered to be eligible for the policy if all their charges for a particular case were misdemeanors or could be found in the statute bank. Since the policy targets non-violent felonies — misdemeanors were already dismissed prior to the policy implementation — defendants who committed only misdemeanor crimes were not considered policy eligible. 

- Policy Applied Criteria: Any charge that was eligible for the policy and had a disposition status matching one of the items in a list provided by the ODDA were considered to have had the policy applied. 


| Policy Applied Disposition                     |
|------------------------------------------------|
| Dismissed                                      |
| Dismissed Completed Pretrial Diversion         |
| Dismissed Converted                            |
| Dismissed Restrict                             |
| Dismissed Restricted                           |
| Nolle Prosse Converted                         |
| Nolle Prosse Restrict                          |
| Not Presented to Grand Jury Restrict           |
| Not Presented to Grand Jury Restrict Converted |
| Pre Trial Diversion Restrict                   |

- Grouping Criteria: To see whether the policy is impacting recidivism rates, a comparison between the defendants with charges flagged as policy eligible by prosecutors and unflagged defendants with similar charges is necessary. Thus, the eligible defendants were divided as such: the treatment group is composed of defendants flagged by a prosecutor as policy eligible and had the policy applied the control group are those not flagged by a prosecutor as policy eligible but who have charges that meet the eligibility criteria and those flagged as eligible but did not have the policy applied. The former will heretofore be referred to as the policy eligible, policy applied population and the latter as the policy eligible, policy not applied population (see Appendix Item 5).

|                | Policy Applied | Policy Not Applied |
|----------------|----------------|--------------------|
| Recidivist     | 46             | 212                |
| Not Recidivist | 1416           | 5036               |

## Plots
Figure 1 displays the average case management time in days for charges disposed on a given disposition date from 2017 to 2023. Case management time was trending downward (i.e. processing efficiency was improving) until around March of 2020, at which point case management time increased drastically. Levels have remained high since the onset of the pandemic.
Figure 2 shows the number of policy eligible and policy applied charges disposed on a given date from March 2020 until 2023. The number of eligible and applied charges has consistently increased, and there is a noticeable gap in between the number of eligible and the number of applied charges, although the distance varies with time. 

![Picture2.png](image%2FPicture2.png) Fig. 1 Average case management time in days
![Picture1.png](image%2FPicture1.png) Fig 2 Charges per month classified as policy eligible and policy applied

Figures 3 and 4 depict the crime characteristics for the recidivist crimes for defendants who had a case dismissed under the policy. Most of the recidivist charges were felonies (72.1%), followed by misdemeanors (24.0%) and a small set of serious felonies (3.9%), the most severe crimes which are ineligible for the policy. The five most frequent recidivist charges were for drug possession, shoplifting, theft by taking, possession of a firearm or knife in the commission of a crime and possession of a firearm by a felon or person on probation. 

![Picture3.png](image%2FPicture3.png) 
![Picture4.png](image%2FPicture4.png)

Fig. 3 & 4 For recidivists who had the policy applied, the crime severity and five most frequent statutes associated with the charges of their recidivist arrests

Figures 5 and 6 show the same information, but for the recidivists who were eligible for the policy but did not have it applied. Although this population committed around the same proportion of felonies, there were slightly more serious felonies (6.5%) and fewer felonies (69.3%). The five most frequent charges were quite similar, as the two groups had four crimes in common and drug possession as the most frequent. Aggravated assaults were represented with higher frequency in the not applied group, and the crimes were committed at more similar frequencies than they were in the policy applied group.

![Picture5.png](image%2FPicture5.png)
![Picture6.png](image%2FPicture6.png)

Fig. 5 & 6 For recidivists who did not have the policy applied, the crime severity and five most frequent statutes associated with the charges of their recidivist arrests

## Statistical Significance

The results of the Z-test revealed that, given the time that has elapsed thus far, the policy does not have a significant effect on recidivism rates. The recidivism rate for the policy eligible, policy applied group was 0.032% and the rate for the policy eligible, policy not applied group was 0.042%. The Z-test value was -1.63, indicating that the null hypothesis can not be rejected. However, given that the Z-test value was negative, it appears as though the policy is trending towards lowering recidivism rates. By continuing to keep the same values constant but increasing the size of n1 and n2 according to their growth rates, it is estimated that an additional 223 days, or around 7.5 months, of additional data collection is needed to be sure whether or not the policy’s effects are significant. At that point in time, statistical significance will reveal itself if it exists (i.e. if the observed differences are the true differences). 

## Interpretation and Conclusion
The three facets of our analysis — prosecutorial efficiency, defendant outcomes and demographic disparities — suggest that the policy is not compounding the ODDA’s workload, but the effects on the DeKalb County community’s overall well-being are less clear. The year 2020 was a complicated year for the criminal justice system — the onset of the pandemic in March 2020, which coincided with the policy implementation, forced the ODDA to shut down yet also exacerbated crime rates. Additionally, the widespread racial justice protests that occurred across the United States following the death of George Floyd and other Black citizens at the hands of law enforcement led to more arrests for violent crimes, which are not policy-eligible. The unique circumstances surrounding the policy’s origin explain the initial decrease in policy-eligible crimes at the beginning of 2020, However, the subsequent increase in policy eligible crimes suggests that the policy did play a more prominent role in the midst of the pandemic. The number of policy-eligible charges disposed per month has grown since the policy’s implementation, and the corresponding increase in the number of charges for which the policy was applied indicates that the policy is diverting more and more eligible defendants from the criminal justice system.
As stated in the Introduction section, increased contact and punitiveness within the criminal justice system does not reduce crime rates or severity, the general public often have the misconception that lenient prosecutorial practices increase criminal activity and decrease community safety. It is difficult to tell on which side of the debate the ODDA’s policy lands — the percentage of felony charges in the overall data set is around 33%, and that percentage jumped to just over 40% for the charges committed by defendants who were previously charged with crimes but had at least one of their previous charges flagged as policy-eligible. The pie chart appears to suggest that, if defendants are re-arrested, their second batch of charges are more likely to contain serious, violent crimes than before. Furthermore, the percentage of recidivists committing felonies exceeds that of the general defendant population. However, Figure 1 only represents 26.7% of the total recidivists; the vast majority of recidivists did not have their first charge flagged as policy-eligible. It is encouraging to note that policy-eligible defendants do not compose the majority of recidivists, yet it is concerning that their crime severity increases upon subsequent arrests.
Consequently, we had to determine on our own which defendants had multiple arrests, and given that many of the observations in the original data sets had missing values it was likely an imperfect classification. Having verified recidivism data would allow for a more confident and cleaner analysis of how DeKalb County recidivism rates have fluctuated since the policy implementation.

# Future Work
Much of the causal inference work related to the overall crime and recidivism rates within DeKalb County was out of the scope of this study due to a lack of accessible data. Recidivism data at non per annum time intervals at the county level is not publicly accessible, and the ODDA was not able to provide any of their own. The current results can only speak to recidivism rates within DeKalb County. Given that addresses covering 50 states are represented in the defendant demographics, including available recidivism and prior criminal record data is critical for more accurately tracking defendant outcomes and uncovering the true effects of the policy.
Similarly, we were unable to examine individual-level effects since the individual’s identifying information was withheld for confidentiality purposes. Tracking defendants in the time period following their arrests allows for incredibly fine-grained data on their economic outcomes, general health and community reintegration post-disposition. Examining county-level trends is a fine proxy, but future work should aim to follow-up with defendants who had cases dismissed under the policy to truly get a sense of the degree to which the policy influenced their lives in the two to five years following. Examining contact with the criminal justice system — arrests, convictions, incarcerations — during that period and conducting interviews surrounding their social, economic and personal health will form a full quantitative and qualitative picture of dismissed defendants’ outcomes and whether they can be traced back to the policy.
While the analyses can be valuable indicators of the ways in which the policy is beginning to sway the criminal justice landscape in DeKalb County, the policy’s effects will be much more noticeable and can be calculated with greater confidence the larger the time period since the policy implementation becomes. The effects of mass incarceration are not always felt immediately, but they can alter the course of the lives of defendants, defendants’ families and community members for years after they have ceased contact with the criminal justice system. Monitoring the individuals contained in the ODDA’s data sets in the 5-10 years following their releases may be a long process that will not provide immediate answers to the ODDA’s most pressing questions, but the data collected is invaluable in that it provides a direct link between the the policy and those whom it affected.
There are also some statistical attempt to evaluate the effect of the policy using time series analysis. Two methods we adopt are structure break and interrupted time series. The first is statistical inference detecting break in time series, the other is the quasi-experimental design for policy effect evaluation. Unfortunately, these methods can not distinguish policy effect from other influencing factor due to the limited nature of time series analysis and design. The result and code will be stored in "Addition" under the image folder.

# Acknowledgements

These notebooks were created by Claire Fenton, Annie Luo, and Feiyu Xiang,. This project wouldn't have been possible without the support from Dr. Blake Fleischer, Office of DeKalb County District Attorney, and Emory University QTM Department. These notebooks were built using the R and Python statistical program.
