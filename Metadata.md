# Additional metadata for SailfishOS:Chum

### Introduction

The basic specification for the additional metadata is [that of AppStream](https://freedesktop.org/software/appstream/docs/chap-Metadata.html#spec-component-filespec).
While it is a goal to leverage AppStream metadata directly for SailfishOS:Chum packages and the SailfishOS:Chum GUI application, we are not at that stage yet, and are instead using a method of embedding metadata in the `%description` section of the RPM spec file.

Note that it is important, that the part from the `%if 0%{?_chum}` to the `%endif` is the last and a contiguous paragraph of the `%description` section, i.e., it must not contain empty or comment lines (or any other line, which is evaluated to an empty line).
If you need comment lines for remarks with regard to the SailfishOS:Chum metadata, place them outside of the whole metadata paragraph, as shown in the example below.

Also note that embracing the metadata for SailfishOS:Chum by `%if 0%{?_chum}` / `%endif` is not strictly necessary: If the `%if…` and `%endif` lines are both omitted, the metadata for SailfishOS:Chum is displayed as part of the package description by common tools as `pkcon`, `zypper`, `rpm` etc.
Nevertheless, metadata for SailfishOS:Chum always must be contiguous (i.e., without lines which are empty or may be evaluated to become empty) and the last paragraph of the `%description` section.

### An example
```
%description
A camera application for Sailfish OS, which provides advanced features. 

# This description section includes metadata for SailfishOS:Chum, see
# https://github.com/sailfishos-chum/main/blob/main/Metadata.md
%if 0%{?_chum}
Title: Advanced Camera
Type: desktop-application
DeveloperName: Adam Pigg
Categories:
 - Media
 - Video
Custom:
  Repo: https://github.com/piggz/harbour-advanced-camera
PackageIcon: https://github.com/piggz/harbour-advanced-camera/raw/master/harbour-advanced-camera.svg
Screenshots:
 - https://github.com/piggz/harbour-advanced-camera/raw/master/screenshots/screenshot1.png
 - https://github.com/piggz/harbour-advanced-camera/raw/master/screenshots/screenshot2.png
 - https://github.com/piggz/harbour-advanced-camera/raw/master/screenshots/screenshot3.png
Links:
  Homepage: https://github.com/piggz/harbour-advanced-camera
  Help: https://github.com/piggz/harbour-advanced-camera/discussions
  Bugtracker: https://github.com/piggz/harbour-advanced-camera/issues
  Donation: https://www.paypal.me/piggz
%endif
```

## Field Descriptions

### Notes
* All fields are optional, and the example above does not use all possible fields (e.g., it lacks a `PackagingRepo:` tag).
* The table below documents version 1 of the SailfishOS:Chum metadata definition.<br />
  Note that four tags of the [original version 0](https://github.com/sailfishos-chum/main/blob/3a24059591d75529cf52d29c5d6a8a8f63feb4c6/Metadata.md) are deprecated [due to issues](https://github.com/sailfishos-chum/main/issues/100), but [still valid as synonyms](https://github.com/sailfishos-chum/sailfishos-chum-gui/pull/181) to the four tags which superseded them in version 1.

### Table of field Descriptions

| Tag                              | Field description                                          | Notes |
| -------------------------------- | ---------------------------------------------------------- | ----- |
| Title:                           | Human readable application name                            | Might comprise multiple words, must be a single line with less than ca. 24 characters.  If not set, the package name in the spec file preamble is used for creating a pretty name.<sup>[1](https://github.com/sailfishos-chum/sailfishos-chum-gui/blob/main/src/chumpackage.cpp#L122-L188)</sup>  Does not follow AppStream specification due to conflicting with Jolla's [`tar_git` service](https://github.com/MeeGoIntegration/obs-service-tar-git) used by SailfishOS-OBS. |
| Type:                            | Basic application type                                     | Defaults to `generic`, unless the package name starts with `harbour-`, then it defaults to `desktop-application`.  See [freedesktop.org:AppStream-docs:YAML-field-dep11](https://www.freedesktop.org/software/appstream/docs/sect-AppStream-YAML.html#field-dep11-type) for valid entries. |
| DeveloperName:                   | Developer's preferred name                                 | If not set, and a GitHub repository is set, then the name will be automatically retrieved.  Note that such automatic retrieval is not ([yet](https://github.com/sailfishos-chum/main/issues/81)) supported for GitLab repositories. |
| PackagedBy:                      | Packager's preferred name                                  | Use if different from the developer and is expected to be contacted for packaging issues.  Defaults to the packager name provided in the spec file preamble, if set there. | 
| Categories:                      | List of categories in which the package will be displayed  | Defaults to `- Other`; see [freedesktop.org:AppStream-docs:ct-categories](https://www.freedesktop.org/software/appstream/docs/chap-CollectionData.html#tag-ct-categories) for the general specification and [specifications.freedesktop.org:menu-spec:apa](https://specifications.freedesktop.org/menu-spec/latest/apa.html) for valid categories. |
| Custom:                          | Root entry for custom repository fields                    |       |
| &nbsp;&nbsp;&nbsp;Repo:          | URL of the source code repository                          | If `Repo:` is set, other URLs for the SailfishOS:Chum GUI application will be automatically determined when possible (see `Links:` sub-fields).  Currently supported are GitHub and GitLab.com URLs in the form `https://github.com/<username>/<reponame>` and `https://gitlab.com/<username>/<reponame>`.<br />If `Repo:` (and `PackagingRepo:`, see below) is not set or the metadata for SailfishOS:Chum is completely missing, the URL provided by the `URL:` field in the spec file preamble is used instead. |
| &nbsp;&nbsp;&nbsp;PackagingRepo: | URL of the repository specifically used for packaging      | Is shown in the SailfishOS:Chum GUI application as a web-link.  If `Repo:` is not set, it is also used as a fallback for the GitHub and GitLab integration. |
| &nbsp;&nbsp;&nbsp;DescriptionMD: | URL for a package description in MarkDown syntax           | If provided, a description is downloaded from the specified URL and rendered as MarkDown in [Showdown's Markdown syntax](https://github.com/showdownjs/showdown/wiki/Showdown's-Markdown-syntax).<br />Otherwise (as default), the description in the `%description` section of the RPM spec file is used. |
| PackageIcon:                     | URL to an image to be displayed in the SailfishOS:Chum GUI application as package icon; may differ from an application's launcher icon. | If not set, no icon will be shown for this package.<br />SVG is the preferred format, PNG the recommended raster format, BMP, GIF, JPG, PBM, PGM, PPM, XBM, XPM [are also supported](https://doc.qt.io/qt-5/qimagereader.html#supportedImageFormats), and ICNS, JP2, MNG, TGA, TIFF, WBMP, WEBP [might be supported](https://doc.qt.io/qt-5/qtimageformats-index.html).  If a raster format is used, the image size should be 172x172 pixels or more, up to 256x256 pixels. |
| Screenshots:                     | List of URLs to screenshots of the application             | If not set, no screenshots will be displayed for the package.  Each URL should be provided in a single line and prefixed by `- ` (dash & space). |
| Links:                           | Root entry for additional URLs                             | These URL fields are displayed in the SailfishOS:Chum GUI application. |
| &nbsp;&nbsp;&nbsp;Homepage:      | URL to the application homepage                            | Overrides the `Repo:` URL if set.  This URL is also probed for the GitHub and GitLab integration after probing the URL provided by custom field `Repo:`. |
| &nbsp;&nbsp;&nbsp;Help:          | URL to an application help page, e.g., a forum             | If not set, and `Repo:` or `Homepage:` is set and points to GitHub, the GitHub discussion page will be used for projects which have it switched on. |
| &nbsp;&nbsp;&nbsp;Bugtracker:    | URL to a bug tracker which allows users to file bugs       | If not set, and `Repo:` or `Homepage:` is set and points to supported repository type, the repository's issues page will be used. |
| &nbsp;&nbsp;&nbsp;Donation:      | URL to a web page proposed for donations                   |       |
