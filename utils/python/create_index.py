from tabulate import tabulate


index_content = '''
# Introduction

## About the experiment

We often look for differences in our surrounding objects to establish a sense of uniqueness that is
associated with each of these objects. The experiment is designed to understand how the visual cortex
differentiate objects. We, therefore, choose a subset of Telugu characters for this behavioural
experiment, wherein, we ask participants to rate the characters based on their perceived dissimilarity
between the glyphs that are displayed.

We do not expect participants to read, speak, or write the Telugu language. How such a participant
with no knowledge of the language perceives differences is the point behind the experiment. People
who know Telugu are also encouraged to participate in the experiment as it will be interesting to
compare the perceived dissimilarity of such participants against the participants who have no idea
of the language.

## Versions of experiment

There are two version of the experiment that were conducted. The only different between the two versions
is the **scale** that was used. The scales are given below:

1. Agreesive scale (&alpha; version/ version 1)
    * Very Dissimilar
    * Dissimilar
    * Neutral
    * Similar
    * Very Similar

1. Passive scale (&beta; version/ version 2)
    * Dissimilar
    * Slightly Dissimilar
    * Neutral
    * Slightly Similar
    * Similar

Version 1 was conducted in a monitered fashion at the AI lab, while version 2 was conducted as an
online survey.

## Instructions

The instructions given for both the version of the experiment are the same. The instructions are
given below:

* You will be shown a pair of Telugu characters for a duration of **2 seconds**, after which
they disappear.
* You are required to rate the pair, in terms of their **Dissimilarity**.
* Once you have rated the pair, click the next button, to get a new pair
* 30 pairs make up a set. You will have to attempt 10 such sets.
* The estimated time of completion for 10 sets is about **25 minutes**.

## About the participants

In version 1 of the experiment, all the participants are form university of Hyderabad. We used their
registration number as an unique indentifier for these participants.

Since version 2 of the experiment was condcuted as an online survey and, we have used their email IDs
as a unique identifier.

## Distribution of the Participants

### Version &alpha;

{alpha_table}

### Version &beta;

{beta_table}

'''


def create_index(ver1, ver2):
    table1 = [
        ['Participants in $\\alpha$ version', len(ver1)]
    ]
    table2 = [
        ['Participants in $\\beta$ version', len(ver2)]
    ]
    tel_ver1 = [0, 0, 0]
    tel_ver2 = [0, 0, 0]
    for user in ver1:
        if ver1[user]['userInfo']['content']['read'] == 'Yes':
            tel_ver1[0] += 1

        if ver1[user]['userInfo']['content']['speak'] == 'Yes':
            tel_ver1[1] += 1

        if ver1[user]['userInfo']['content']['write'] == 'Yes':
            tel_ver1[2] += 1

    for user in ver2:
        if ver2[user]['userInfo']['content']['read'] == 'Yes':
            tel_ver2[0] += 1

        if ver2[user]['userInfo']['content']['speak'] == 'Yes':
            tel_ver2[1] += 1

        if ver2[user]['userInfo']['content']['write'] == 'Yes':
            tel_ver2[2] += 1
    table1.append(['Telugu participants', max(tel_ver1)])
    table1.append(['Telugu readers', tel_ver1[0]])
    table1.append(['Telugu speakers', tel_ver1[1]])
    table1.append(['Telugu writers', tel_ver1[2]])

    table2.append(['Telugu participants', max(tel_ver2)])
    table2.append(['Telugu readers', tel_ver2[0]])
    table2.append(['Telugu speakers', tel_ver2[1]])
    table2.append(['Telugu writers', tel_ver2[2]])

    page = open('docs/README.md', 'w+')
    page.write(index_content.format(
        alpha_table=tabulate(
            table1, headers=['Data', 'Value'], tablefmt='github'),
        beta_table=tabulate(
            table2, headers=['Data', 'Value'], tablefmt='github'))
    )
    page.close()
