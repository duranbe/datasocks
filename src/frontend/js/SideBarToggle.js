function SideBarToggle(){
        var sidebar = document.getElementById("accordionSidebar");
        var currentclass =sidebar.className;
        if (currentclass.includes("toggled")) {
          sidebar.className = currentclass.replace(' toggled','')
        } else {
          sidebar.className = currentclass+' toggled'
        }
        
      }