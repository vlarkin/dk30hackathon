# Slack-Bot for Preview Environment Automation

This bot automates the creation, management, and deletion of preview environments directly from your Slack workspace. Powered by Slack Machine, our bot helps you turn your Slack workspace into a powerful ChatOps system.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Creating a Slack App](#creating-a-slack-app)
3. [Configuration](#configuration)
4. [Setup and Installation](#setup-and-installation)
5. [Running the Bot](#running-the-bot)
6. [Commands](#commands)

## Getting Started

To get started, you need to create a new Slack app and configure it to work with Slack Machine. Follow the steps below to set up everything you need.

## Creating a Slack App

1. Go to [Slack API Apps](https://api.slack.com/apps).
2. Choose "Create New App" from an App Manifest.
3. Copy and paste the following manifest:

    ```yaml
    display_information:
      name: EnvBot
    features:
      bot_user:
        display_name: EnvBot
        always_online: false
    oauth_config:
      scopes:
        bot:
          - app_mentions:read
          - channels:history
          - channels:join
          - channels:read
          - chat:write
          - chat:write.public
          - emoji:read
          - groups:history
          - groups:read
          - groups:write
          - im:history
          - im:read
          - im:write
          - mpim:history
          - mpim:read
          - mpim:write
          - pins:read
          - pins:write
          - reactions:read
          - reactions:write
          - users:read
          - users:read.email
          - channels:manage
          - chat:write.customize
          - dnd:read
          - files:read
          - files:write
          - links:read
          - links:write
          - metadata.message:read
          - usergroups:read
          - usergroups:write
          - users.profile:read
          - users:write
    settings:
      event_subscriptions:
        bot_events:
          - app_home_opened
          - app_mention
          - channel_archive
          - channel_created
          - channel_deleted
          - channel_id_changed
          - channel_left
          - channel_rename
          - channel_unarchive
          - group_archive
          - group_deleted
          - group_left
          - group_rename
          - group_unarchive
          - member_joined_channel
          - member_left_channel
          - message.channels
          - message.groups
          - message.im
          - message.mpim
          - reaction_added
          - reaction_removed
          - team_join
          - user_change
          - user_profile_changed
          - user_status_changed
      interactivity:
        is_enabled: true
      org_deploy_enabled: false
      socket_mode_enabled: true
      token_rotation_enabled: false
    ```

4. Add the Slack App and Bot tokens to your `local_settings.py` like this:

    ```python
    SLACK_APP_TOKEN = "xapp-my-app-token"
    SLACK_BOT_TOKEN = "xoxb-my-bot-token"
    ```

## Configuration

For security considerations, you can use environment variables instead of storing tokens in your source code. Prefix the setting name with `SM_`:

```sh
export SM_SLACK_APP_TOKEN="xapp-my-app-token"
export SM_SLACK_BOT_TOKEN="xoxb-my-bot-token"
```

## Setup and Installation

1. Create a virtual environment and activate it:

    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```

2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Running the Bot

To start the bot, run:

```sh
slack-machine
```

## Commands

### Create a Preview Environment

Create a new preview environment by telling the bot:

```
/create <name_env> <branch_or_hash_commit>
```

### View Current Preview Environments

View the current state of all created preview environments using:

```
/get
```

### Delete a Preview Environment

Delete a specific preview environment by specifying to the bot:

```
/delete <name_env>
```
