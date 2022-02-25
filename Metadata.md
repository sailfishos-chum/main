# Additional metadata for SailfishOS:Chum

The basic specification for the additional metadata is that of AppStream.
While it is a goal to leverage AppStream metadata directly for SailfishOS:Chum packages and the SailfishOS:Chum GUI application, we are not at that stage yet, and are instead using a method of embedding metadata in the "Description" field of the rpm spec file.
Note that it is important, that the part from the `%if "%{?vendor}" == "chum"` to the `%endif` is the last and a contiguous sub-section of the `%description` section, i.e., it must not contain empty or comment lines (or any other line, which is evaluated to an empty line).
If you need comment lines for remarks with regard to the SailfishOS:Chum metadata, place them before the `%if`.

An example of how this is done follows:
```
%description
Better camera application

# This description section includes metadata for SailfishOS:Chum, see
# https://github.com/sailfishos-chum/main/blob/main/Metadata.md
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
Note: All fields are optional, and the example above does not use all possible fields (e.g., `PackagingRepo:`).

| Field name                 | Description                                                | Notes |
| -------------------------- | ---------------------------------------------------------- | ----- |
| PackageName:               | Human readable application name                            | If not set, it is calculated from the package ID.  Does not follow AppStream specification due to clash with OBS tar\_git service. |
| Type:                      | Basic application type                                     | Defaults to `generic`, unless the package name starts with `harbour-`, then it defaults to `desktop-application`.  See [freedesktop.org:AppStream-docs:YAML-field-dep11](https://www.freedesktop.org/software/appstream/docs/sect-AppStream-YAML.html#field-dep11-type) for valid entries. |
| DeveloperName:             | Developer's preferred name                                 | If not set, and a GitHub repository is set, then name will be automatically retrieved.  Note that such automatic retrieval is not supported for GitLab repositories. |
| PackagerName:              | Name of the packager                                       | Use if different from the developer and is expected to be contacted for packaging issues. | 
| Categories:                | List of categories in which the package will be displayed  | Defaults to `- Other`; see [freedesktop.org:AppStream-docs:ct-categories](https://www.freedesktop.org/software/appstream/docs/chap-CollectionData.html#tag-ct-categories) for the general specification and [specifications.freedesktop.org:menu-spec:apa](https://specifications.freedesktop.org/menu-spec/latest/apa.html) for valid categories. |
| Custom:                    | Root entry for custom repository fields                    |       |
| &nbsp;&nbsp;Repo:          | URL of the source code repository                          | If `Repo:` is set, other URLs for SailfishOS:Chum GUI application will be automatically determined when possible (see `Url:` sub-fields).  Currently supported are GitHub and GitLab.com URLs in the form `https://github.com/<username>/<reponame>` and `https://gitlab.com/<username>/<reponame>`. |
| &nbsp;&nbsp;PackagingRepo: | URL of the repository specifically used for packaging      | Is shown in the SailfishOS:Chum GUI application as a web-link.  If `Repo:` is not set, it is used as a fallback for the GitHub and GitLab integration. |
| &nbsp;&nbsp;DescriptionMD: | URL for a package description in MarkDown syntax           | If provided, a description is downloaded from the specified URL and rendered as MarkDown (see [Showdown's-Markdown-syntax](https://github.com/showdownjs/showdown/wiki/Showdown's-Markdown-syntax)). |
| Icon:                      | URL to an image used for the application icon              | If not set, no icon will be displayed in the SailfishOS:Chum GUI application for the package.  Supported file formats are SVG and PNG. |
| Screenshots:               | Array of URLs to screenshots of the application            | If not set, no screenshots will be displayed for the package. |
| Url:                       | Root entry for additional URLs                             | These URL fields are displayed in the SailfishOS:Chum GUI application. |
| &nbsp;&nbsp;Homepage:      | URL to the application homepage                            | Overrides the `Repo:` URL if set.  This URL is probed for GitHub and GitLab support after probing the URL provided by custom field `Repo:`. |
| &nbsp;&nbsp;Help:          | URL to an application help page, e.g., a forum             | If not set, and `Repo:` or `Homepage:` is set and points to GitHub, the GitHub discussion page will be used for projects which have it switched on. |
| &nbsp;&nbsp;Bugtracker:    | URL to a bug tracker which allows users to file bugs       | If not set, and `Repo:` or `Homepage:` is set and points to supported repository type, the repository issues page will be used. |
| &nbsp;&nbsp;Donation:      | URL to a page allowing to donate to the developer          |       |
