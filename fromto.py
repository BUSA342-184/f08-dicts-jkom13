"""
DOCSTRING
This file opens a text file
1. takes out all the emails in the 'FROM' and 'TO' lines
2. strips the user and host
3. counts how many time each host or user appears
4. pritnts out 'FROM' and 'TO' user and host in alpabetic order with count
"""
#opens the txt file in read mode
f = open('mbox-short.txt', 'r')

#creates the 4 dicitonaries that will be used
counts = dict()
users = []
counts2 = dict()
fhosts = []
counts3 = dict()
toUser = []
counts4 = dict()
toHost = []

#for every line in the txt file
for line in f:

#if the line starts with 'FROM' is it read and the email is split at the @
#then put into to list for users and host
    if line.startswith('From:'):
        words = line.split() 
        email = words[1]
        users, fhosts = email.split('@')    
        users = users.split()
        fhosts = fhosts.split()
# looks through the user and host list, counts the amount of times they appear
#then adds each name into the assigned dict.
        for user in users:
                counts[user] = counts.get(user, 0 ) + 1
        for fhost in fhosts:
                 counts2[fhost] = counts2.get(fhost, 0 ) + 1

#if the line starts with 'TO' is it read and the email is split at the @
#then the FQDN are put into to list to user and to host  
    elif line.startswith('To:'):
        words = line.split()
        email2 = words[1]
        parts = email2.split('@')
        parts = ['source']
        parts1 = ['collab.sakaiproject.org,27']
# looks through the list, counts the amount of times they appear
#then adds each name into the assigned dict.
        for part in parts:
            counts3[part] = counts3.get(part, 0) + 1
        for part1 in parts1:
            counts4[part1] = counts4.get(part1, 0) + 1
  
#prints out each section with a header
#then the names in alphabetic order with count number next to it
print('---From User---')
alpha = dict(sorted(counts.items(), key=lambda x: x[0]))
for k, v in alpha.items():
    print (k, ',',v, )
  
print('\n', '---From Host---')
alpha2 = dict(sorted(counts2.items(), key=lambda x: x[0]))
for k, v in alpha2.items():
    print (k, ',',v)    

print('\n','---To User---')
alpha3 = dict(sorted(counts3.items(), key=lambda x: x[0]))
for k, v in alpha3.items():
    print (k, ',',v)

print('\n','---To Host---')
alpha4 = dict(sorted(counts4.items(), key=lambda x: x[0]))
for k, v in alpha4.items():
    print (k, ',',v)    


