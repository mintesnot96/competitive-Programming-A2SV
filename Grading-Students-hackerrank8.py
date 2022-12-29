def gradingStudents(grades):
    final_result=[];
    for i in range(0,len(grades)):
        if grades[i]<38:
            final_result.append(grades[i])
        else:
            for j in range(grades[i],grades[i]+5):
                if j%5==0 and j-grades[i]<3:
                    final_result.append(j)
                    break
                elif j%5==0:
                    final_result.append(grades[i])
    return final_result

#   question link
# https://www.hackerrank.com/challenges/grading/problem
