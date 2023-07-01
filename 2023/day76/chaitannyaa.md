# Day 76 Build a Grafana dashboard

A dashboard gives you an at-a-glance view of your data and lets you track metrics through different visualizations.

Dashboards consist of panels, each representing a part of the story you want your dashboard to tell.

Every panel consists of a query and a visualization. The query defines what data you want to display, whereas the visualization defines how the data is displayed.

## Task 01

- In the sidebar, hover your cursor over the Create (plus sign) icon and then click Dashboard.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/a9900778-a8b6-4e72-9057-c5be33094ec5)

- Click Add a new panel.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/8ca21c53-bf48-4483-9960-536ca4971c00)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/f296151b-1504-43f1-ac4b-803d61894c3f)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/b00486bd-1883-45d7-870c-de4bdb8873b3)

- In the Query editor below the graph, enter the query from earlier and then press Shift + Enter:

```sum(rate(http_request_duration_microseconds_count[5m])) by(route)```

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/042b84eb-ce51-4a55-a3af-a81cfc246c56)

- In the Legend field, enter {{route}} to rename the time series in the legend. The graph legend updates when you click outside the field.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/32124f2e-9005-4ad9-a978-096abb08a36d)

- In the Panel editor on the right, under Settings, change the panel title to “Traffic”.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/445b03d7-2520-4e39-9bb7-b00237fad439)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fd8cd0dd-0f4b-40dd-b2c0-ec6164acbf5e)

- Click Apply in the top-right corner to save the panel and go back to the dashboard view.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fd4634ae-79e2-427e-9e37-a0c120f34abf)

- Click the Save dashboard (disk) icon at the top of the dashboard to save your dashboard.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/87740b38-3cc8-4577-abc8-21fbccbd765a)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/fb752095-e2e1-4935-8d9c-36c3e2e56fe9)

- Enter a name in the Dashboard name field and then click Save.

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/ea1229a1-4cae-43b5-97ee-0af7710c2bf7)

![image](https://github.com/Chaitannyaa/90DaysOfDevOps/assets/117350787/d7591415-32fc-49f2-8f38-45d83a9193d9)

Happy Learning :)

# Day 76 task is done!
