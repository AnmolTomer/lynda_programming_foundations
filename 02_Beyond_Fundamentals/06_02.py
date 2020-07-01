infile = open('values.txt', 'rt')

outfile = open("values-totaled.txt", 'wt')

print('Processing Input:\n')
sum = 0
for line in infile:
    sum += int(line)
    print(line.rstrip(), file=outfile)

print("\nTotal: " + str(sum), file=outfile)
outfile.close()
print('Output Complete')
# Set following in your json as true: "python.terminal.executeInFileDir": true
# It tells python that when program mentions another file it should look in same directory for other file.
