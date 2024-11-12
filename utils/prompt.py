SplitPrompt = '''
Strictly follow the format of the below examples,
Use "the answer is" to give the answer. Before giving the answer, imagine what sub-questions there are in this 
question(Different problems have different reasoning processes，So these question 
has different numbers of sub-problems). Give the reasoning process 
like a chain according to a logical relationship. 
Mark each sub-question of the reasoning process with a serial number, 
according to the following format:

Q: In which year was the director who won the Oscar for Best Picture in 2015 born?
A: q1: Which movie is the Oscar for Best Picture in 2015?
a1: The Oscar for Best Picture in 2015 is "Birdman".
q2: Who is the director of "Birdman"?
a2: The director of "Birdman" is Alejandro González Iñárritu.
q3: In which year was Alejandro González Iñárritu born?
a3: Alejandro González Iñárritu was born on August 15, 1963.
the answer is August 15, 1963

'''
