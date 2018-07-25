

def find(source_lsit, target):

   temp = dict()
   result = dict() # save result
   rindex = 0      # result index

   for i in range(len(source_list)):  # go over whole source_list
        
         if int(source_list[i]) <= target:    # if element great then traget, then skip it
 
            temp[source_list[i]] = i          # save element for lookup candidate, temp[key] is the value of element in source_list, temp[value] is the index of element in source_lsit

            candidate = target - int(source_list[i])    # get candidate 

            if candidate in temp.keys():                # search candidate from temp{}

               result[rindex] = [ temp[candidate], i]   # if any, save index in result{}
               rindex = rindex + 1                      # keep search other combination

   return result



source_list = (0, 66, 44, 22, 43, 12, 465, 76, 33, 55)
target = 55

print (find(source_list, target))
