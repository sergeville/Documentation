The URL format you provided, `http://localhost:8123/todo?entity_id=todo.shopping_list`, suggests you are interacting with a **Home Assistant** instance, specifically trying to access the **Shopping List** to-do entity.

While you can **view** the list using a URL like that (if accessed from within your network), you cannot **add a task** directly to the list using a simple **GET** request to that URL in a web browser.

To add a task to a Home Assistant to-do list entity like `todo.shopping_list`, you need to use the Home Assistant **Service Call** mechanism, which typically involves an **API request** (often a **POST** request) or using the user interface.

-----

## 🛠️ Methods to Add a Task

The most common and effective ways to add an item are:

### 1\. Using Home Assistant's UI (The Simplest Way)

The easiest way is to use the dedicated **Shopping List** card or the **To-Do List** card within the Home Assistant frontend, where you can simply type in the new item and press Enter.

### 2\. Using the Home Assistant Services Menu

You can manually call the service in the Developer Tools:

1.  Go to **Developer Tools** in your Home Assistant sidebar.

2.  Navigate to the **Services** tab.

3.  For the **Service** field, select: `todo.add_item`.

4.  In the **Target** field, select your entity: `todo.shopping_list`.

5.  In the **Service Data (YAML)** section, enter the item name:

    ```yaml
    item: Buy milk
    ```

6.  Click **CALL SERVICE**.

### 3\. Using the Home Assistant REST API

For third-party integrations, scripts, or advanced automation, you would send a **POST** request to the Home Assistant API endpoint, for example:

  * **URL:** `http://localhost:8123/api/services/todo/add_item`

  * **Method:** `POST`

  * **Headers:**

      * `Authorization`: `Bearer YOUR_LONG_LIVED_ACCESS_TOKEN`
      * `Content-Type`: `application/json`

  * **Body (JSON):**

    ```json
    {
      "entity_id": "todo.shopping_list",
      "item": "New item to buy"
    }
    ```

**Note:** You must have a **Long-Lived Access Token** to authenticate API requests. This is a secure method and cannot be done by simply typing a URL into your browser's address bar.
