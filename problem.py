__author__ = 'Kalyan'

notes = '''
fval of a string is defined as sum of ordinals of characters of string. 

For e.g. fval of A is 65, fval of AA is 130

You are given a file of words. You have to create a new file in the following format

word1 : friendword1
word2 : friendword2
....

friendword of a word is a word which has the closest fval to the given word in the input 
file of words. 

Notes:

1. write it as a main script to be run from command line
2. input and output words files should be taken from command line.
3. words should be written in dictionary order
4. write good readable code

Some updates to the spec will be given 45 minutes into the test, so structure your code 
so that you can update it easily as the spec changes.
'''
import sys
def find_fval(word):
    return sum([ord(letter) for letter in word])
def group_words(input_filename):
    words=[line.strip() for line in open(input_filename,"r") if line.strip()!=""]
    words=sorted(words,key=lambda x:(find_fval(x),x.lower()))
    return words
def write_into_output(output_filename,words,frnd_no):
    with open(output_filename,"w") as fd:
        for index in range(0,words.__len__()):
            if(index==0):
                print(words[index]+" : "+words[index+1]+"\n")
                fd.write(words[index]+" : "+words[index+1]+"\n")
            elif(index==words.__len__()-1):
                print(words[index] + " : " + words[index - 1] + "\n")
                fd.write(words[index]+" : "+words[index-1]+"\n")
            elif((find_fval(words[index])-find_fval(words[index-1]))>=(find_fval(words[index+1])-find_fval(words[index]))):
                print(words[index]+" : "+words[index+1]+"\n")
                fd.write(words[index]+" : "+words[index+1]+"\n")
            elif((find_fval(words[index])-find_fval(words[index-1]))<=(find_fval(words[index+1])-find_fval(words[index]))):
                print(words[index] + " : " + words[index - 1] + "\n")
                fd.write(words[index]+" : "+words[index-1]+"\n")
    pass
def write_into_outputk_dict(ouput_filename,words,frnd_no):
    with open(output_filename, "w") as fd:
        for index in range(0, words.__len__()):
            if (index == 0):
                fd.write(words[index] + " : ")
                for i in range(0, frnd_no):
                    fd.write(words[i + 1] + " ")
                fd.write("\n")
            else:
                fd.write(words[index] + " : ")
                i = index - 1
                j = index + 1
                count = 0
                while (1):
                    if (i >= 0 and j < words.__len__() and (find_fval(words[index]) - find_fval(words[i])) == (find_fval(words[j]) - find_fval(words[index]))):
                        if(words[i].lower()>words[j].lower()):
                            fd.write(words[j]+" ")
                            j=j+1
                            count+=1
                        else:
                            fd.write(words[i] + " ")
                            i=i-1
                            count+=1
                    elif (i >= 0 and j < words.__len__() and (find_fval(words[index]) - find_fval(words[i])) > (
                        find_fval(words[j]) - find_fval(words[index]))):
                        fd.write(words[j] + " ")
                        j = j + 1
                        count += 1
                    elif (i >= 0 and j < words.__len__() and (find_fval(words[index]) - find_fval(words[i])) < (
                        find_fval(words[j]) - find_fval(words[index]))):
                        fd.write(words[i] + " ")
                        i -= 1
                        count += 1
                    elif (i < 0):
                        while (1):
                            fd.write(words[j] + " ")
                            j = j + 1
                            count += 1
                            if (count == frnd_no):
                                break
                    elif (j >= words.__len__()):
                        while (1):
                            fd.write(words[i] + " ")
                            i = i - 1
                            count += 1
                            if (count == frnd_no):
                                break
                    if (count == frnd_no):
                        break
                fd.write('\n')
def write_into_outputk(output_filename,words,frnd_no):
    with open(output_filename,"w") as fd:
        for index in range(0,words.__len__()):
            if(index==0):
                print(words[index]+":")
                fd.write(words[index]+" : ")
                for i in range(0,frnd_no):
                        print(words[index] + ":")
                        fd.write(words[i + 1] +" ")
                fd.write("\n")
            else:
               fd.write(words[index] + " : ")
               i=index-1
               j=index+1
               count=0
               while(1):
                   if (i>=0 and j<words.__len__() and (find_fval(words[index])-find_fval(words[i]))==(find_fval(words[j])-find_fval(words[index]))):
                       fd.write(words[i] + " ")
                       i =i- 1
                       count += 1
                   elif(i>=0 and j<words.__len__() and (find_fval(words[index])-find_fval(words[i]))>(find_fval(words[j])-find_fval(words[index]))):
                       fd.write(words[j] + " ")
                       j=j+1
                       count+=1
                   elif(i>=0 and j<words.__len__() and (find_fval(words[index])-find_fval(words[i]))<(find_fval(words[j])-find_fval(words[index]))):
                       fd.write(words[i] + " ")
                       i -= 1
                       count+=1
                   elif(i<0):
                       while(1):
                           fd.write(words[j] + " ")
                           j = j + 1
                           count += 1
                           if(count==frnd_no):
                                break
                   elif(j>=words.__len__()):
                       while (1):
                           fd.write(words[i] + " ")
                           i= i - 1
                           count+= 1
                           if (count == frnd_no):
                               break
                   if(count == frnd_no):
                       break
               fd.write('\n')



pass
if __name__ == "__main__":
    input_filename =sys.argv[1]
    #input_filename="input.txt"
    words=group_words(input_filename)
    output_filename=sys.argv[2]
    k=int(sys.argv[3])
    #k=1
    #output_filename="output2.txt"
    write_into_outputk_dict(output_filename,words,k)
    #write_into_outputk(output_filename, words,k)
    pass



