# Assignment 1.1 - Rules of Engagement

## Question 1:

Review section 1.5.2 (a-i) Conducting the Pen Test.  

What is the focus and intent of these steps?  What seems to be the priorities?

The focus is on how to conduct a pentest without disrupting business operation. Before begiining a pentest, you must establish clear communication channels, gain formal authorization, and be controlled in the execution of pentest activities. The section emphasizes documentation and incremental reporting rather than aggressive exploitation. Policy review, compliance, and documentation tasks are equally as important to technical exploitation.

## Question 2:

Review Appendix A. - Penetration Test Plan

How does this Plan relate to the Attack Methodology we covered in class? How does it correspond to the Course Syllabus?

It maps to the kill chain methodology. "Planning and Enumeration" corresponds to reconnaissance and scanning phases. "Vulnerability Analysis" aligns with enumeration and vulnerability scanning. "Penetration Testing" covers exploitation, post-exploitation, and reporting phases. The methodology follows a progression from passive information gathering to active exploitation to analysis and remediation.

## Question 3:

Review Appendix B. Rules to be Followed

Identify 2 rules that may limit the testers from fully identifying all potential vulnerabilities. Briefly explain why NASA requires these limitations.

```
[Third party's] test procedures will use non-destructive testing techniques (i.e., no files or data
on the target systems are to be modified, added, deleted, or changed). Evidence to support any
access control weaknesses discovered should consist primarily of screen prints and session logs.
```
In a real attack, the attacker would be able to modify and change files in the system for persistence, privilege escalaction, and exfiltration.


```
Under no circumstances will a network or system compromise at NASA be exploited that
results in the penetration of one or more of NASA's corporate or govemment partners'
```
While this is a good rule for liability reasons, an attacker might be able to find vulnerabilities in partner organizations that are attack vectors into NASAs network.


## Question 4: Optional

What is War Dialing?

War dialing is a reconnaissance technique that dials ranges of telephone numbers to identify devices connected to phone lines (modems, fax machines) that could provide unauthorized network access. The scanning tool tries to find which numbers answer with carrier tones, then adds the number as a potential attack vector.

