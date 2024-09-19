This article contains all actions for retrieving and managing rules.

# Get rule by ID

=== "Query"
    ```graphql
    query {
      getRule(id: "1") {
        id
        siteid
        type
        label
        provider
        datestart
        dateend
        config
        position
        status
        mtime
        ctime
        editor
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      getRule(id: "1") {
        id
        siteid
        type
        label
        provider
        datestart
        dateend
        config
        position
        status
        mtime
        ctime
        editor
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      getRule(id: "1") {
        id
        siteid
        type
        label
        provider
        datestart
        dateend
        config
        position
        status
        mtime
        ctime
        editor
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

Response:

```json
{
  "data": {
    "getRule": {
      "id": "1",
      "siteid": "1.",
      "type": "catalog",
      "label": "+10% Test",
      "provider": "Percent",
      "datestart": null,
      "dateend": null,
      "config": "{\\"last-rule\\":0,\\"percent\\":10}",
      "position": 0,
      "status": 1,
      "mtime": "2022-12-22 09:51:38",
      "ctime": "2022-06-21 13:36:28",
      "editor": "aimeos@aimeos.org"
    }
  }
}
```

# Search rules

The filter parameter is explained in the [filter section](basics.md#filtering-the-result) of the [GraphQL basics](basics.md) article.

=== "Query"
    ```graphql
    query {
      searchRules(filter: "{\\"~=\\": {\\"rule.label\\":\\"Test\\"}}") {
        items {
          id
          siteid
          type
          label
          provider
          datestart
          dateend
          config
          position
          status
          mtime
          ctime
          editor
        }
        total
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      searchRules(filter: "{\\"~=\\": {\\"rule.label\\":\\"Test\\"}}") {
        items {
          id
          siteid
          type
          label
          provider
          datestart
          dateend
          config
          position
          status
          mtime
          ctime
          editor
        }
        total
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    let filter = {
        "~=": {"rule.label":"Test"}
    };
    const fstr = JSON.stringify(JSON.stringify(filter));
    const body = JSON.stringify({'query':
    `query {
      searchRules(filter: ` + fstr + `) {
        items {
          id
          siteid
          type
          label
          provider
          datestart
          dateend
          config
          position
          status
          mtime
          ctime
          editor
        }
        total
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

Response:

```json
{
  "data": {
    "searchRules": {
      "items": [
        {
          "id": "1",
          "siteid": "1.",
          "type": "catalog",
          "label": "+10% Test",
          "provider": "Percent",
          "datestart": null,
          "dateend": null,
          "config": "{\\"last-rule\\":0,\\"percent\\":10}",
          "position": 0,
          "status": 1,
          "mtime": "2022-12-22 09:51:38",
          "ctime": "2022-06-21 13:36:28",
          "editor": "aimeos@aimeos.org"
        }
      ],
      "total": 1
    }
  }
}
```

# Fetch rule configuration

To retrieve the backend configuration for a rule provider and the added decorators use:

=== "Query"
    ```graphql
    query {
      getRuleConfig(provider: "Percent,Category", type: "catalog") {
        code
        type
        label
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      getRuleConfig(provider: "Percent,Category", type: "catalog") {
        code
        type
        label
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `query {
      getRuleConfig(provider: "Percent,Category", type: "catalog") {
        code
        type
        label
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

Response:

```json
{
  "data": {
    "getRuleConfig": [
      {
        "code":"last-rule",
        "type":"boolean",
        "label":"Don't execute subsequent rules"
      },{
        "code":"percent",
        "type":"number",
        "label":"Percentage to add or subtract"
      },{
        "code":"category.code",
        "type":"string",
        "label":"Category codes"
      }
    ]
  }
}
```

# Save single rule

=== "Mutation"
    ```graphql
    mutation {
      saveRule(input: {
        type: "catalog"
        label: "Test rule"
        provider: "Percent"
        config: "{\\"percent\\": 10}"
      }) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`query {
      saveRule(input: {
        type: "catalog"
        label: "Test rule"
        provider: "Percent"
        config: "{\\"percent\\": 10}"
      }) {
        id
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveRule(input: {
        type: "catalog"
        label: "Test rule"
        provider: "Percent"
        config: "{\\"percent\\": 10}"
      }) {
        id
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

Response:

```json
{
  "data": {
    "saveRule": {
      "id": "2"
    }
  }
}
```

# Save multiple rules

=== "Mutation"
    ```graphql
    mutation {
      saveRules(input: [{
        type: "catalog"
        label: "Test rule 2"
        provider: "Percent"
        config: "{\\"percent\\": 10}"
      }
      {
        type: "catalog"
        label: "Test rule 3"
        provider: "Percent,Category"
        config: "{\\"percent\\":20,\\"category.code\\":\\"demo-best\\"}"
      }]) {
        id
      }
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      saveRules(input: [{
        type: "catalog"
        label: "Test rule 2"
        provider: "Percent"
        config: "{\\"percent\\": 10}"
      }
      {
        type: "catalog"
        label: "Test rule 3"
        provider: "Percent,Category"
        config: "{\\"percent\\":20,\\"category.code\\":\\"demo-best\\"}"
      }]) {
        id
      }
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      saveRules(input: [{
        type: "catalog"
        label: "Test rule 2"
        provider: "Percent"
        config: "{\\"percent\\": 10}"
      }
      {
        type: "catalog"
        label: "Test rule 3"
        provider: "Percent,Category"
        config: "{\\"percent\\":20,\\"category.code\\":\\"demo-best\\"}"
      }]) {
        id
      }
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

Response:

```json
{
  "data": {
    "saveRules": [
      {
        "id": "3"
      },
      {
        "id": "4"
      }
    ]
  }
}
```

# Delete single rule

=== "Mutation"
    ```graphql
    mutation {
      deleteRule(id: "2")
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteRule(id: "2")
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteRule(id: "2")
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

Response:

```json
{
  "data": {
    "deleteRule": "2"
  }
}
```

# Delete multiple rules

=== "Mutation"
    ```graphql
    mutation {
      deleteRules(id: ["3", "4"])
    }
    ```
=== "JQAdm"
    ```javascript
    Aimeos.query(`mutation {
      deleteRules(id: ["3", "4"])
    }`).then(data => {
      console.log(data)
    })
    ```
=== "Javascript"
    ```javascript
    const body = JSON.stringify({'query':
    `mutation {
      deleteRules(id: ["3", "4"])
    }`});

    fetch('<GraphQL URL>', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { // Laravel only
            'X-CSRF-TOKEN': '<CSRF token>'
        },
        body: body
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    });
    ```

Response:

```json
{
  "data": {
    "deleteRules": [
      "3",
      "4"
    ]
  }
}
```
