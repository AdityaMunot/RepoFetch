import requests
import json


def Urldata(URL):
    html = requests.get(URL)
    loaded_json = json.loads(html.text)
    return loaded_json


def Repocheck(UserID):
    URL = 'https://api.github.com/users/'+UserID+'/repos'
    Data = Urldata(URL)
    repos = []
    for x in Data:
        if "name" in x:
            repos.append([x["name"]])
    for i in repos:
        URL = "https://api.github.com/repos/"+UserID+"/"+i[0]+"/commits"
        Data = Urldata(URL)
        commit = 0
        for x in Data:
            if "commit" in x:
                commit = commit + 1
        i.append(commit)
    return repos


def Repoprint(repos):
    for i in repos:
        print(f"Repo: {i[0]} Number of commits: {i[1]}")
    print(repos)


def main():
    UserID = input("Enter GitHub user ID: ")
    repos = Repocheck(UserID)
    Repoprint(repos)

# Uncomment this below line to use this py file
#if __name__ == "__main__":
#    main()