# Additional metadata guidance for the chum store

The standard for app store metadata is Appstream.  While it is a goal to investigate using appstream metadata for chum packages and the chume gui (store) we are not yet at that stage, and are instead using a method of embedding metadata in the rpm .spec "Description" field.  An example of how this can be done is below:

```
%description
Better camera application

%if "%{?vendor}" == "chum"
    packagename: Advanced Camera
    type: desktop-application
    developername: Adam Pigg
    categories:
     - Media
     - Video
    custom:
     - repotype: github
     - repo: https://github.com/piggz/harbour-advanced-camera
    icon: https://raw.githubusercontent.com/piggz/harbour-advanced-camera/master/harbour-advanced-camera.svg
    screenshots:
     - https://github.com/piggz/harbour-advanced-camera/raw/metadata/screenshots/screenshot1.png
     - https://github.com/piggz/harbour-advanced-camera/raw/metadata/screenshots/screenshot2.png
     - https://github.com/piggz/harbour-advanced-camera/raw/metadata/screenshots/screenshot3.png
    url:
     - homepage: https://github.com/piggz/harbour-advanced-camera
     - help: https://github.com/piggz/harbour-advanced-camera/discussions
     - bugtracker: https://github.com/piggz/harbour-advanced-camera/issues
     - donation: https://www.paypal.me/piggz
%endif
```

## Field Descriptions

Note: All fields are optional


| Field                          | Description                                                                                                                 | Notes                                                                                                                                                                                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PackageName                    | Human readable application name                                                                                             | If not set, calculated from the package id. Doesnt follow Appstream spec due to clash with OBS tar\_git service                                                                                                                                       |
| Type                           | Basic application type.                                                                                                     | Defaults to desktop-application. See [https://www.freedesktop.org/software/appstream/docs/sect-AppStream-YAML.html#field-dep11-type](https://www.freedesktop.org/software/appstream/docs/sect-AppStream-YAML.html#field-dep11-type) for valid entries |
| DeveloperName                  | Developers preferred name.                                                                                                  | If not set, and a github/lab repo is set then name will be automatically retrieved                                                                                                                                                                    |
| Categories                     | Array of store categories where the application will be displayed                                                           | Defaults to "Other" See [https://www.freedesktop.org/software/appstream/docs/chap-CollectionData.html#tag-ct-categories](https://www.freedesktop.org/software/appstream/docs/chap-CollectionData.html#tag-ct-categories)                              |
| Custom<br>\-RepoType<br>\-Repo | Two custom fields are suported, RepoType and Repo. RepoType can be github or gitlab, and Repo is the URL of the repository. | If these are set, data for the store will be retrieved automatically where possible                                                                                                                                                                   |
| Icon                           | URL to an image used in the store for the application icon                                                                  | If not set, no icon will be visible                                                                                                                                                                                                                   |
| Screenshots                    | Array of URLs to screenshots of the application                                                                             | If not set, no screenshots will be displayed                                                                                                                                                                                                          |
| URL                            | Array of other URLs for the store entry as below                                                                            |                                                                                                                                                                                                                                                       |
| \-Homepage                     | URL to application homepage                                                                                                 | Overrides repo URL if set                                                                                                                                                                                                                             |
| \-Help                         | URL to application help, eg a forum                                                                                         | If not set, and a repo is set, the repo discussion page will be used                                                                                                                                                                                  |
| \-Bugtracker                   | URL to bug tracker to allow user to file bugs                                                                               | If not set, and a repo is set, the repo issues page will be used                                                                                                                                                                                      |
| \-Donation                     | URL to a page allowing a donation to the developer                                                                          |                                                                                                                                                                                                                                                       |


