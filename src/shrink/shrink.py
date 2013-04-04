import json
import requests

def get_issues(user, repo, state):
    """
    Retrieve the GitHub issues for the specified user & repo
    """
    base_url = 'https://api.github.com/repos/'
    separator = '/'
    url = base_url+user+separator+repo+separator+'issues'
    
    issues = requests.get(url+'?'+state)
    return json.loads(issues.text)

if __name__ == "__main__":
    user = 'siwells'
    repo = 'monkeypuzzle'
    
    print "Num Open Issues: ", len(get_issues(user, repo, 'open'))
    print "Num Closed Issues: ", len(get_issues(user, repo, 'closed'))
    
