
"""
Just some functions to help build websites faster.
Most everything is done in the idea of using Bootstrap4, but you can alter this to some extent. 
  Goal: Reformat the builder functions with different themes in mind
  
"""


def buildBasicHtmlPage(theme="bootstrap4"):
    """Builds a very basic HTML skeleton, based on different plug in themes.
        Theme is set to Bootstrap4, but can also have Pure.io, Material-UI, or Basscss,
        just set paramter theme to whichever opensource framework you want to build"""
    theme = theme.lower()

    if theme == "bootstrap4" or "bootstrap":
        print("""
        <!DOCTYPE html>
          <head>
            <!-- Bootstrap 4 (https://getbootstrap.com/) -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
            <title></title>
          </head>
          <body>

            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
          </body>
        </html>
""")

    elif theme == "pure" or "pure.css":
        print("""
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <!-- Pure.CSS (https://purecss.io/start/) -->
            <meta charset="utf-8">
            <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/pure-min.css" integrity="sha384-nn4HPE8lTHyVtfCBi5yW9d20FjT8BJwUXyWZT9InLYax14RDjBj46LmSztkmNP9w" crossorigin="anonymous">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title></title>
          </head>
          <body>

          </body>
        </html>
""")
    elif theme == "material-ui" or "material":
        print("""
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <!-- Material - UI (https://material-ui.com/) -->
            <meta charset="utf-8">
            <script src="https://unpkg.com/@material-ui/core/umd/material-ui.production.min.js" crossorigin="anonymous"></script>

            <!-- Roboto Font -->
            <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500">

            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title></title>
          </head>
          <body>

          </body>
        </html>
""")


    elif theme == "basscss" or "bass":
        print("""
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <!-- Basscss (http://basscss.com) -->
            <meta charset="utf-8">
            <link href="https://unpkg.com/basscss@8.0.2/css/basscss.min.css" rel="stylesheet">

            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title></title>
          </head>
          <body>

          </body>
        </html>
""")


def buildOrderedList(listOfLi, orderedClass="", itemClass=""):
    """Builds an ordered list out of provided listOfLi, add orderedClass or itemClass to customize"""
    print(f"<ol class='{orderedClass}'>")
    for li in listOfLi:
        print(f"\t<li>{li}</li>")
    print("</ol>")
    return


def buildUnorderedList(listOfLi, orderedClass="", itemClass=""):
    """Builds an unordered list out of provided listOfLi, add orderedClass or itemClass to customize"""

    print(f"<ul class='{orderedClass}'>", orderedClass)
    for li in listOfLi:
        print(f"<li>{li}</li>")
    print("</ul>")
    return


def buildSideBar(sidebarItems=[], sideBarTitle="Sidebar Title", textUnderTitle="", titleTag="h3", outmostDivClass="list-group", unorderedListClass= "list-group", listItemClass="list-group-item"):
    """Builds a basic sidebar,
    add a list to sidebarItems and it'll generate a sidebar to that size,
    built with Bootstrap4 in mind"""
    print(f"""
    <div class="{outmostDivClass}">
      <div class="content-section">
        <{titleTag}>{sideBarTitle}</titleTag>
        <p class='text-muted'>{textUnderTitle}</p>
          <ul class="{unorderedListClass}">
""")
    for li in sidebarItems:
        print(f"""\t\t<li class="{listItemClass}">{li}</li>""")
    print("""
        </ul>
      </div>
    </div>
""")



def buildNavigationAtHeader(itemsOnLeftSideURL=[], itemsOnLeftSideText=[], itemsOnRightSideURL=[], itemsOnRightSideText=[], navClass="navbar navbar-expand-md navbar-dark fixed-top", aClass="nav-item nav-link"):
    """Builds a basic navigation header that is responsive to the page,
    add a list of items and urls for the left side or right side and it'll build it accordingly,
    built with Bootstrap4 in mind"""

    print(f"""
    <header class="site-header">
      <nav class={navClass}>
        <div class="container">
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarToggle">""")

    if itemsOnLeftSideText != []:
        print("""\t\t<div class="navbar-nav mr-auto">""")
        for item, url in zip(itemsOnLeftSideText, itemsOnLeftSideURL):
            print(f"""\t\t\t<a class={aClass} href="/{url}">{item}</a>""")
        print("""\t\t</div>""")

    if itemsOnRightSideText != []:
        print("""\t\t<div class="navbar-nav">""")
        for item, url in zip(itemsOnRightSideText, itemsOnRightSideURL):
                print(f"""\t\t\t<a class={aClass} href="/{url}">{item}</a>""")
        print("""\t\t</div>""")

    print("""
          </div>
        </div>
      </nav>
    </header>
""")
