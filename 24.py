import os
from github import Github

#access_token = input( "enter acess token")
token = os.environ.get("GIT_TOKEN")
#org_name = os.environ.get("ORGNAME")
#g = Github(access_token)
g = Github(token)

#org_name = "siriguppavenkatsai"

##g = Github(base_url="https://siriguppavenkatsai/api/v3", login_or_token="access_token")

#repo = g.get_organization("siriguppavenkatsai").get_repo("V") 


for repo in g.get_organization($org).get_repos(): 
#for repo in g.get_user().get_repos(): 
 for branch in repo.get_branches():
        b = repo.get_branch(branch.name)
        
        
        if b.protected:
              
              print("repository name is", repo.name,"and  branch name is", b.name ,"(protected)")
              
              #print("Required status check is",b.get_required_status_checks())
              print("ADmin enforcement is",b.get_admin_enforcement())
              print("Team push restrictions is",b.get_team_push_restrictions())
              print("Pull requests reviews are",b.get_required_pull_request_reviews())
              print("Signatures are",b.get_required_signatures())
              print("push restrictions are",b.get_user_push_restrictions())
              
        else:
            print("repository name is ", repo.name,"and  branch name is", b.name ,"(unprotected)")
