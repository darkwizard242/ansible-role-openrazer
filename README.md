[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-openrazer.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-openrazer) ![Ansible Role](https://img.shields.io/ansible/role/43078?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43078?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43078?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-openrazer&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-openrazer) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-openrazer?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-openrazer?color=orange&style=flat-square)

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

Variable                        | Value (default)        | Description
------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------
openrazer_repo                  | 'ppa:openrazer/stable' | Refers to the ppa repo to add.
openrazer_repo_desired_state    | present                | Defined to dynamically chose whether to add/keep (i.e. `present`) or remove (i.e. `absent`) the repository file list from `/etc/apt/sources.list.d`.
openrazer_repo_filename         | openrazer              | Defined to set the repository file name for saving in `/etc/apt/sources.list.d`
openrazer_app                   | openrazer-meta         | Defines the app to install i.e. **openrazer-meta**
openrazer_package_desired_state | present                | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default is set to `present`.

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
