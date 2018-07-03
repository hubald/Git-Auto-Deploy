import re
from .base import WebhookRequestParserBase

class VstsRequestParser(WebhookRequestParserBase):

    def get_matching_projects(self, request_headers, request_body, action):
        import json

        data = json.loads(request_body)

        repo_urls = []
        pattern = re.compile(r"^https:\/\/(?P<host>\w+)\.visualstudio\.com\/(?P<project>\w+)\/_git\/(?P<code>\w+)$");

        action.log_debug("Received event from VSTS")

        try:
            url = data['resource']['repository']['remoteUrl']
            parts = re.findall(pattern, url)
            ssh_url = 'ssh://%s@vs-ssh.visualstudio.com:22/%s/_ssh/%s' % (result[0][0], result[0][1], result[0][2])
            
            repo_urls.append(ssh_url)
            repo_configs = self.get_matching_repo_configs(repo_urls, action)

            return repo_configs
        except KeyError:
            action.log_error("Unable to recognize data format")
            return []
