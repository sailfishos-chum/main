# Additional metadata guidance for the chum store

The standard for app store metadata is Appstream.  While it is a goal to investigate using appstream metadata for chum packages and the chume gui (store) we are not yet at that stage, and are instead using a method of embedding metadata in the rpm .spec "Description" field.  An example of how this can be done is below:

```
%description
Better camera application

%if "%{?vendor}" == "chum"
PackageName: Advanced Camera
Type: desktop-application
DeveloperName: Adam Pigg
Categories:
 - Media
 - Video
Custom:
  Repo: https://github.com/piggz/harbour-advanced-camera
Icon: https://raw.githubusercontent.com/piggz/harbour-advanced-camera/master/harbour-advanced-camera.svg
Screenshots:
 - https://github.com/piggz/harbour-advanced-camera/raw/metadata/screenshots/screenshot1.png
 - https://github.com/piggz/harbour-advanced-camera/raw/metadata/screenshots/screenshot2.png
 - https://github.com/piggz/harbour-advanced-camera/raw/metadata/screenshots/screenshot3.png
Url:
  Homepage: https://github.com/piggz/harbour-advanced-camera
  Help: https://github.com/piggz/harbour-advanced-camera/discussions
  Bugtracker: https://github.com/piggz/harbour-advanced-camera/issues
  Donation: https://www.paypal.me/piggz
%endif
```

## Field Descriptions

Note: All fields are optional


| Field                          | Description                                                                                                                 | Notes                                                                                                                                                                                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PackageName                    | Human readable application name                                                                                             | If not set, calculated from the package id. Doesn't follow Appstream spec due to clash with OBS tar\_git service                                                                                                                                       |
| Type                           | Basic application type.                                                                                                     | Defaults to `generic` unless package name starts with `harbour-` when it defaults to `desktop-application`. See [https://www.freedesktop.org/software/appstream/docs/sect-AppStream-YAML.html#field-dep11-type](https://www.freedesktop.org/software/appstream/docs/sect-AppStream-YAML.html#field-dep11-type) for valid entries |
| DeveloperName                  | Developers preferred name.                                                                                                  | If not set, and a GitHub repo is set then name will be automatically retrieved. Note that such automatic retrieval is not supported for GitLab repositories                                                                                                                                                                 |
| PackagerName                  | Name of the packager. | Use if different from the developer and is expected to be contacted for Sailfish packaging issues      | 
| Categories                     | Array of store categories where the application will be displayed                                                           | Defaults to "Other" See [https://www.freedesktop.org/software/appstream/docs/chap-CollectionData.html#tag-ct-categories](https://www.freedesktop.org/software/appstream/docs/chap-CollectionData.html#tag-ct-categories)                              |
| Custom<br>&nbsp;&nbsp;Repo | Repo is the URL of the repository. Currently supported are GitHub and GitLab.com in the form `https://github.com/...` and `https://gitlab.com/...`. | If repository is set, data for the store will be retrieved automatically where possible                                                                                                                                                                   |
| Custom<br>&nbsp;&nbsp;PackagingRepo | PackagingRepo is the URL of the repository used for packaging. | Is shown in UI as a link. If main project repository is not indicated, is used as a fallback for GitHub and GitLab integration |
| Icon                           | URL to an image used in the store for the application icon                                                                  | If not set, no icon will be visible                                                                                                                                                                                                                   |
| Screenshots                    | Array of URLs to screenshots of the application                                                                             | If not set, no screenshots will be displayed                                                                                                                                                                                                          |
| Url                            | Object of other URLs for the store entry as below                                                                            |                                                                                                                                                                                                                                                       |
| &nbsp;&nbsp;Homepage                     | URL to application homepage                                                                                                 | Overrides package URL if set. This URL is probed for GitHub and GitLab support after probing URL given by custom field `Repo`                                                                                                                                                                                                                             |
| &nbsp;&nbsp;Help                         | URL to application help, eg a forum                                                                                         | If not set, and `Repo` or `URL` is set and point to GitHub, GitHub discussion page will be used for projects that have discussion forum posts.                                                                                                                                                                                 |
| &nbsp;&nbsp;Bugtracker                   | URL to bug tracker to allow user to file bugs                                                                               | If not set, and `Repo` or `URL` is set and points to supported repository type, the repository issues page will be used                                                                                                                                                                                      |
| &nbsp;&nbsp;Donation                     | URL to a page allowing a donation to the developer                                                                          |                                                                                                                                                                                                                                                       |


