function LiveColorChange(inputId,dotID){
        var input = document.getElementById(inputId);
        var dot = document.getElementById(dotID)
        dot.style.backgroundColor = input.value;
      }