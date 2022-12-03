# Intro

### Ella or Min are you able to do the intro as you are both a bit more into the pyscology stuff?

# EDA

### During the exploratory data analysis of this project, the data was manipulated in different ways for each question because it was important for the data to reflect what was being looked at. However, there were a few main steps that were common among each. For starters, each member looked at the size of the overall data as well as what was included in this data, including the column names, data types, and stats of each type of data included. While looking at this it was found that there were some unanswered questions throughout the data, such as a zero for the race or gender data, or a very large number for the age data. This data was removed before the team members removed the columns they would not be needing for their questions. Once the data had been cleaned and unusable data had been filtered out each member created graphs from their data to try to get a sense of how to answer their questions. While looking at differences in ages vs personality traits this is one of the graphs created. Insert a graph here. Looking into the difference between males and females regarding personality traits, this graph was used as a starting point. Insert graph here. And the final question about differences in race and personality traits leads to graphs like this one. Insert graph here.

# Question 1 - How do the 5 different personality factors change over different age groups?

# Question 2 - How do scores between males and females differ on the 5 personality factors?
## **Hypothesis**: Based on extant research, on average, females will show higher scores than men on Extraversion, and Agreeableness, lower scores on Neuroticism, and there are will be no significant gender differences for Conscientiousness or Openness.
<br>

### You can find the [full analysis notebook here](./notebooks/analysis2.ipynb), including the code and data
<br>

![Barplot by gender](./images/barbygender.png)

## **Figure 1**

This plot shows the mean factor scores for each of the 5 factors, separated by gender. 

This plot is a good starting point to see roughly where there are gender differences in the data. For instance, it is evident that men show higher scores than females on Openness and Neuroticism (emotional stability) while females show higher scores on Extraversion and Agreeableness. However, this plot is not the easiest to interpret since the bars for the same factor are not beside each other. Figure 3 will show side-by-side comparisons of means to make the analysis a bit easier. 

Although not a part of the research questions, I found it interesting that the pattern of scores were similar in some ways (e.g., both genders showed higher scores on Agreeableness, Conscientiousness, and Openness than Extraversion and Neuroticism (emotional stability); both genders showed the highest scores for Agreeableness and Openness. However, males showed higher scores on Neuroticism than extraversion whereas females showed higher scores on Extraversion than Neuroticism (emotional stability) and males showed higher scores on Openness than Agreeableness whereas females showed higher scores on Agreeableness than Openness. 
<br>
<br><br><br><hr />

![Boxplot](./images/boxplot.png)

## **Figure 2**

Box plots showing the median (50th percentile), 25th percentile, and 75th percentile of each of the 5 factors, separated by gender. The bottom line of the box represents the 25th percentile, the middle line in the box represents the median, and the upper line of the box represents the 75th percentile. All together, the box represents the middle 50% of the data points and is referred to as the interquartile range (IQR). The lines extending from the boxes represent 1.5x the IQR and are indicative of the spread of the data -- that is, how closely clustered the individual data points are to the average. 

In this plot, the lines for Extraversion and Neuroticism extend all the way to the minimum and maximum scores, indicating a large amount of variation (i.e., spread) in the data. The plots for Agreeableness, Conscientiousness, and Openness extend to the maximum but not to the minimum. This is likely because the distribution for these factors is negatively skewed (i.e., clustered more closely to the high end of the continuum). The diamond points below the line indicate outliers in the data which are simply determined by being outside of the IQR. Based on the large sample size, skew of the data, and nature of the constructs being measured, the outliers were not removed since they are likely "true outliers" that represent natural variation in the data (e.g., it is not unreasonable that some individuals will have much lower scores on some factors than other individuals). 

This plot is useful because it gives a lot of information about the averages and distribution of the data. For instance, it can be used to compare median scores between genders which is useful for answering the research question. Based on this plot, males showed higher average scores on Neuroticism and Openness while females showed higher average scores on Extraversion, Agreeableness, and Conscientiousness. 
<br><br><br><hr />

![Barplot](./images/barplot.png)
## **Figure 3**

Bar plot showing the mean factor scores for each of the 5 factors, separated by gender. Error bars represent 98% confidence intervals. 

Compared to Figure 1, this plot makes it easier to see the differences between factor scores for each gender. It is clear that Extraversion and Neuroticism have lower average scores while Agreeableness and Openness have higher average scores than the other factors, for both genders. When comparing between genders, the error bars representing the confidence intervals can be helpful for determining whether the difference in group means is significant -- that is, if the error bars overlap with one another, it is likely that the difference between group means is not significant. For the current research, the only factor that has error bars close to overlapping is Conscientiousness. This is in line with the hypothesis that Conscientiousness would not show significant gender differences. The other proposed null relationship was between gender and Openness -- while this factor does appear to show gender differences, the magnitude is less than that of the other 3 factors (i.e., E, N, and A). Therefore, it appears that the data show support for the hypothesis that there are gender differences among the Extraversion, Neuroticism, and Agreeableness factors. 
<br><br><br><hr />

# Question 3 - How do scores between all races differ on the five personality factors? Furthermore, is there a relationship between personality traits and race?

## **Hypothesis**:
I hypothesized that a particular race group would show higher scores on the big five personality traits (extraversion, neuroticism, agreeableness, conscientiousness, openness) than other race group.
<br>

### You can find the [full analysis notebook here](./notebooks/analysis3.ipynb), including the code and data
<br>

![Barplot by Race](./images/Race%20Bar%20Plot1.png)
## **Figure 1**
This bar plot shows the mean factor scores for each of the five personality traits, separated by race. All races show higher scores on agreeableness and openness and lower scores on extraversion and neuroticism. Scores on conscientiousness are in the middle for all races.
<br><br><br><hr />

![Barplot by Race](./images/Race%20Bar%20Plot2.png)
## **Figure 2**
This plot shows Pearson's correlation coefficient among the five personality traits for each race. The darker colours represent a greater magnitude of correlation. All races show a weak positive correlation or no correlation among the five personality traits.
<br><br><br><hr />

![Correlation Plot by Race](./images/Race%20Correlation.png)
## **Figure 3**
The American Indian or Alaska Native shows the strongest correlation (r = .42) between Extraversion and Agreeableness and the weakest correlation (r = .10) between Neuroticism and Openness. Asian shows the strongest correlation (r = .35) between Extraversion and Agreeableness and the weakest correlation (r = .11) between Neuroticism and Openness. Black or African American shows the strongest correlation (r = .34) between Agreeableness and Conscientiousness and the weakest correlation (r = .049) between Extraversion and Conscientiousness. Native Hawaiian or Other Pacific Islander shows the strongest correlation (r = .33) between Agreeableness and Conscientiousness and the weakest correlation (r = .026) between Neuroticism and Agreeableness. White shows the strongest correlation (r = .34) between Extraversion and Agreeableness and the weakest correlation (r = .059) between Openness and Conscientiousness. No particular correlation between personality traits is strongest or weakest for all races.

However, all races show a stronger correlation between Extraversion and Agreeableness compared to other correlations between personality traits. Moreover, all races show a weaker correlation between Neuroticism and Openness and between Conscientiousness and Openness compared to other correlations between personality traits.

# Conclusion 

### Stuff in brackets is notes for you guys to read, not part of the paragraph. 

### Looking into the five main personality traits versus different factors has shown that (I’m not quite sure if there is a summation as I haven’t in detailed checked your guy's stuff, but I was thinking something along the lines of) there are not many links between these factors and the different traits. Every individual person scores differently on OCEAN (fill in the full names of these things later) no matter their age, sex, or race. (Not sure if we really need to mention the skewed data here, if not replace “It is important … it can still” with “This can”) It is important to remember that much of this data was skewed by a large majority of the participants being young, white females, but it can still be seen by looking at the age groups versus personality scores and seeing that the average scores of each group were similar to each other. When looking at the traits split between male and female it was shown that ______. Finally, while looking to see if there was a link between race and personality traits it could be seen that _________.

### Another option would start with...

###  Looking into the five main personality traits versus different factors has shown that there are not many differences on personality traits with ____, but there are when looking at ____...

## Question 1
## Question 2 
## Question 3
All races showed higher scores on agreeableness and openness and lower scores on extraversion and neuroticism. Also, scores on conscientiousness were in the middle for all races. All races scored similarly on each of the five personality traits. There was no particular correlation between personality traits that were strongest or weakest for all races. However, all races showed a stronger correlation between extraversion and agreeableness compared to other correlations between personality traits. Also, all races showed a weaker correlation between neuroticism and openness and between conscientiousness and openness compared to other correlations between personality traits. These results indicated no differences in the big five personality traits among races, which did not support the hypothesis.

In conclusion, there was no significant difference in scores between all races on the five personality factors. Furthermore, there was no significant relationship between personality traits and race.
