
function CreateCard(data){

    
    let CardName = data['card_name']
    //let CardDate = new Date(data['card_date']).toLocaleString('fr-FR', { timeZone: 'GMT' });
    let CardId = data['id']
    var newCard = document.createElement("div");

    newCard.className = 'class="col-xl-2 col-md-2 mb-4 col-sm-8 col-8';
    newCard.innerHTML = `
              <div class="card border-left-primary shadow h-100 ">
                <div class="card-body">
                      
                          <div class="h5 font-weight-bold text-primary text-uppercase col-xl-11 text-nowrap" >${CardName}</div>
                          
                          <div class="row">
                              
                              <div class="col-10">
                                <div  id="${CardName}" class="h3 mb-1 font-weight-bold text-gray-800 text-center mt-2"></div>
                              </div>
                              
                              <div class="col-2">
                                
                                <div class="row">
                                

                                  <div class="col">
                                    <div class="dropdown no-arrow">
                                      <a class="dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                        <div style="font-size: 1rem;">
                                        ☰
                                        </div>
                                      </a>
                                      <div class="dropdown-menu dropdown-menu-right shadow animated--fade-in" aria-labelledby="dropdownMenuLink">
                                        <div class="dropdown-header">Action</div>

                                        <a class="dropdown-item" onclick="DeleteElement('cards','${CardId}')" href=''>Delete Card</a>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                              
                                
                            </div>

                          </div>
                          
                         <div id ="${CardName}Date" class="h2 mt-4 text-center"><h6></h6></div>
                </div>
              </div>`

    return(newCard)

}