#By Ken Li, from Hackerrank AI

def displayPathtoPrincess(N,matrix): #required to create displayPathtoPrincess function
    row = {}
    column = {} #first set 2D matrix
    rescue = False #in beginning, bot & princess not in same position

    for i in range(N):
        line = len(matrix[i])
        for j in range(line):
            if matrix[i][j] == 'm': #m is given as represetation of bot, remember using '' for string!
                row['m'] = i
                column['m'] = j #fetch the bot's current position
            elif matrix[i][j] == 'p': #given as representation of princess
                row['p'] = i 
                column['p'] = j #fetch the princess's current position

    while (rescue == False): #when bot & princess not in same position, loop to move
        if row['m'] > row['p']: #if bot has lower position than princess, need to move up
            row['m'] = row['m'] - 1
            print ('UP')
        
        elif row['m'] < row['p']: #if bot has upper position than princess, need to move down
            row['m'] = row['m'] + 1
            print ('DOWN')
         

        if column['m'] > column['p']: #same logic if bot is on princess's right, move left
            column['m'] = column['m'] - 1
            print ('LEFT')
            
        elif column['m'] < column['p']:
            column['m'] = column['m'] + 1
            print ('RIGHT')
        
        
        if row['m'] == row['p'] and column['m'] == column['p']: #when same position, rescued
            rescue = True


m = int(input()) #print out every move as required
matrix = [] 
for i in range(0, m): 
    matrix.append(input().strip())

displayPathtoPrincess(m,matrix)
