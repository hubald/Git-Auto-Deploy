from .base import WebhookRequestParserBase


class VstsRequestParser(WebhookRequestParserBase):

    def get_matching_projects(self, request_headers, request_body, action):
        import json

        data = json.loads(request_body)

        repo_urls = []

        action.log_debug("Received event from VSTS")

        try:
            url = data['resource']['repository']['remoteUrl']
            repo_urls.append(url)
            repo_configs = self.get_matching_repo_configs(repo_urls, action)

            return repo_configs
        except KeyError:
            action.log_error("Unable to recognize data format")
            return []