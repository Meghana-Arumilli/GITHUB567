import requests, json

def get_from_github(username):

    url = 'https://api.github.com/users/' +  username + '/repos'   
    print(url) 
    data = requests.get(url)
    result = []
    # print(data.status_code)
    if data.status_code == 200:
        repos = json.loads(data.text)
        # print(len(repos))
        if len(repos) == 0:
            return 'unable to fetch repos from user'

        for repo in repos:
            repourl = repo['url']
            repodata = requests.get(repourl)
            if repodata.status_code == 200:
                repodata = json.loads(repodata.text)
                commiturl = 'https://api.github.com/repos/' + username + '/' + repodata['name'] + '/commits'
                commitdata = requests.get(commiturl)
                if commitdata.status_code == 200:
                    commitdata = json.loads(commitdata.text)
                    commits = len(commitdata)
                    s = 'Repo: ' + repodata['name'] + ' Number of commits: ' + str(commits)
                    print(s)
                    result.append(s)
            else:
                return 'unable to fetch repos from user'
        return result
    else:
        return 'unable to fetch repos from user'

if __name__ == '__main__':
    result = get_from_github('Meghana-Arumilli')
    print(result)