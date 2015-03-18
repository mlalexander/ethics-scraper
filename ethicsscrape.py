from BeautifulSoup import BeautifulSoup

html = open('page.html', 'r').read()


soup = BeautifulSoup(html)
lobbyists = soup.find('table', attrs={'id': 'ctl00_ContentPlaceHolder_grvMain'})


output = []

# Your scraper should do several things:

# 1. First, grab all the lobbyist expenditures from the table
# 2. Skip, or ignore, the column that says "View"
# 3. If the transaction is for an official in Columbia, add it to the output list
# 4. Remove the &nbsp; string from all output where it appears
# 5. At the end, print the output list

########## YOUR CODE GOES HERE ##########


for tr in lobbyists.findAll('tr'):

    output_row = []

    for td in tr.findAll('td')[1:]:
        row_list = td.text.replace('&nbsp;', '')

        output_row.append(row_list)

        if "Columbia" in row_list:
            print output_row
