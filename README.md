[![build-test](https://github.com/darkwizard242/ansible-role-openrazer/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-openrazer/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-openrazer/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-openrazer/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/openrazer) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-openrazer&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-openrazer) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-openrazer&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-openrazer) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-openrazer&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-openrazer) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-openrazer?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-openrazer?color=orange&style=flat-square)

# Ansible Role: openrazer

Role to install (_by default_) [openrazer-meta](https://openrazer.github.io/) package or uninstall (_if passed as var_) on **Ubuntu** systems for supporting Razer products drivers and customization on Ubuntu systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
openrazer_repo: 'ppa:openrazer/stable'
openrazer_repo_desired_state: present
openrazer_repo_filename: openrazer
openrazer_app: openrazer-meta
openrazer_package_desired_state: present
```

### Variables table:

Variable                        | Description
------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------
openrazer_repo                  | Refers to the ppa repo to add.
openrazer_repo_desired_state    | Defined to dynamically chose whether to add/keep (i.e. `present`) or remove (i.e. `absent`) the repository file list from `/etc/apt/sources.list.d`.
openrazer_repo_filename         | Defined to set the repository file name for saving in `/etc/apt/sources.list.d`
openrazer_app                   | Defines the app to install i.e. **openrazer-meta**
openrazer_package_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default is set to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **openrazer** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.openrazer
```

For customizing behavior of role (i.e. installation of latest **openrazer** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.openrazer
  vars:
    openrazer_package_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **openrazer** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.openrazer
  vars:
    openrazer_package_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-openrazer/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
