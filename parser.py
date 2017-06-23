# This iterator function first yields the string it is called with if it is in words.
# Then it splits the string in two in every possible way.
# If the first part is not in words, it tries the next split.
# If it is, the first part is prepended to all the results of calling itself on the second part
def substrings_in_set(s, words):
    if s in words:
        yield [s]
    for i in range(1, len(s)):
        if s[:i] not in words:
            continue
        for rest in substrings_in_set(s[i:], words):
            yield [s[:i]] + rest


def read_file(filename, filename1):
    #Open the zone file with only read permission
    f = open(filename, 'r')
    #make set of all words which are given in the dictionary
    words = set(x.strip().lower() for x in open(filename1).readlines())
    for i in range (1,10):
     words.add(str(i))
    #From the specific zone file provided for this assesment, to consider all domain names after all time to live (TTL) dicription-
    #-I had initializes variable no_ttl
    no_ttl = 0
    i = 0

    for line in f:
        if no_ttl != 0:
            #Splitting line with respect to '.' can give us the information about domain and second level domain
            s = line.split('.');
            my_list_len = len(s)
            #After that we will check every possible domain from the given zone file to separate
            for t in range(0, my_list_len):
                if (s[t] == 'COM' or s[t] == 'NET' or s[t] == 'INFO' or s[t] == 'DE' or s[t] == 'SK' or s[t] == 'EU' or
                            s[t] == 'TW' or s[t] == 'ORG' or s[t] == "JP" or s[t] == 'CZ' or s[t] == 'CN' or s[t] == 'US' or s[t] == 'NL' or s[t] == 'IT' or s[t] == 'RU' or s[t] == 'BIZ' or s[t] == 'AT'):

                    if (t != 0):
                        #word_find is our SLD
                        word_find = s[t - 1].strip()
                        #now we needs to substract '-' and space from word
                        y = word_find.replace(" ", "").lower()
                        y=y.replace("-",'')


                        d = []
                        no_match = []
                        name = y
                        found = set()
                        for split in substrings_in_set(name, words):
                            found |= set(split)
                        #making list of all possible words from second level domains
                        for word in found:
                            d.append(word)
				        #making list of match not found words.			
                        if not found:
                            no_match.append(name)

                        q = " "
                        r = ""
                        #if there is no value in list then we needs check it
                        if len(d) != 0:

                            q = q.join(d)

                        else:
                            q=y

                        #printing SLD ,domain and list which have we gained from SLD as per given dictionary
                        print("%s.%s=>%s  " % (word_find, s[t], q));
        elif line.startswith('$TTL'):
             no_ttl = no_ttl + 1




if __name__ == '__main__':
    name = raw_input("What is zone file address? ")
    name1 = raw_input("What is dictionary address? ")
    read_file(name, name1)
#"/home/apurv/Downloads/info.zone"
#"/home/apurv/Downloads/dictionary.txt"