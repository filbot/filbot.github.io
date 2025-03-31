+++
date = '2025-03-31T16:34:28-07:00'
draft = false
title = 'AEM Developer Cheat Sheet'
description = 'A quick-start resource I wish I had when I began working with AEM—meant to help new developers get up and running without having to learn everything the hard way on the job.'
tags = ['aem', 'frontend', 'developer-tools', 'aem-resources']
+++

Just a little something I wish I had when I first started working with AEM. Adobe Experience Manager can feel like a real chicken-and-egg situation—Adobe doesn’t provide an easy way to set up AEM instances for experimentation, so you’re kind of forced to learn on the job. That’s a tough spot to be in when a company is paying you to already know how to do AEM work.

## A. Common URLs

| Purpose | Path |
|--------|------|
| AEM Author Login | `http://localhost:4502` |
| AEM Publish Instance | `http://localhost:4503` |
| CRXDE Lite | `/crx/de` |
| Felix Console (OSGi configs/bundles) | `/system/console/configMgr` |
| Sling Models console | `/system/console/adapters` |
| Dispatcher Flush Agent | `/etc/replication/agents.author/dispatcher` |
| Package Manager | `/crx/packmgr/index.jsp` |
| Useradmin | `/useradmin` |
| Sites Authoring | `/sites.html/content` |
| Template Editor | `/libs/wcm/core/content/sites/templates.html/conf` |

## B. Useful File System Paths (JCR)

| Purpose | JCR Path |
|--------|----------|
| Page Content | `/content/your-site/...` |
| Components | `/apps/your-project/components/...` |
| Templates | `/conf/your-project/settings/wcm/templates/...` |
| Editable Template Policies | `/conf/your-project/settings/wcm/policies/...` |
| Core Components (Do not modify!) | `/libs/core/components/...` |
| Clientlibs | `/apps/your-project/clientlibs/...` |
| Designs (for legacy static templates) | `/etc/designs/` |

## C. Maven Commands

```bash
mvn clean install
mvn clean install -PautoInstallPackage
mvn clean install -PautoInstallPackage -pl ui.apps
mvn clean install -PautoInstallBundle -pl core
```

## D. CRX Package Manager (Curl)

```bash
curl -u admin:admin -F file=@"my-package.zip" -F name=my-package -F force=true -F install=true http://localhost:4502/crx/packmgr/service.jsp
```

## E. HTL (Sightly) Snippets

```html
${myModel.title}
<ul data-sly-list.item="${myModel.items}">
  <li>${item.name}</li>
</ul>
<div data-sly-resource="${ 'mycomponent' @ resourceType='myproject/components/foo' }"></div>
<div data-sly-test="${myModel.showThing}">Shown if true</div>
```

## F. Sling Models (Java)

```java
@Model(adaptables = Resource.class)
public class ExampleModel {
    @Inject private String title;
    @ValueMapValue private String subtitle;
    @Default(values = "Default text") private String footer;
    public String getTitle() { return title; }
}
```

## G. Registering an OSGi Servlet

```java
@Component(service = Servlet.class,
           property = {
             "sling.servlet.methods=GET",
             "sling.servlet.paths=/bin/myendpoint"
           })
public class MyServlet extends SlingSafeMethodsServlet {
    @Override
    protected void doGet(SlingHttpServletRequest req, SlingHttpServletResponse resp) throws IOException {
        resp.getWriter().write("Hello from servlet!");
    }
}
```

## H. Dispatcher Caching Quick Tips

- Flush content via flush agent at `/etc/replication/agents.author/dispatcher`
- Debug caching using `X-Cache: HIT/MISS` headers
- Deny example: `/filter { /0001 { /type "deny" /url "*.json" } }`

## I. Troubleshooting Tips

| Symptom | Tip |
|--------|-----|
| Component not rendering | Check `resourceType` and Sling resolution |
| Model not working | Confirm `@Model` and Sling exporter |
| Bundle not active | Check `/system/console/bundles` |
| No logs from code | Use logger, check `error.log` |
| Dispatcher not updating | Clear cache or flush manually |

## J. Log Statements (Java)

```java
private static final Logger log = LoggerFactory.getLogger(MyModel.class);
log.info("Something happened");
log.debug("Variable value: {}", value);
log.error("Something went wrong", e);
```

## K. Common Component File Structure

```
/apps/your-project/components/card/
  ├── card.html
  ├── _cq_dialog/.content.xml
  ├── _cq_editConfig.xml
  └── cq:template
```

## L. Editable Template Setup

1. Template type: `/apps/your-project/templates`
2. Templates: `/conf/your-project/settings/wcm/templates`
3. Policies: `/conf/your-project/settings/wcm/policies`
