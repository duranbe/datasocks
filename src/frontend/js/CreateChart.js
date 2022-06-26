function createGraphCard(data) {
    var newGraph = document.createElement("div");

    if (data['graph_type'] == 'LN') {
      newGraph.className = 'col-xl-9 col-md-2 mb-4';
    } else {
      newGraph.className = 'col-xl-3 col-md-2 mb-4';

    }

    newGraph.innerHTML = `<div class="card shadow mb-4 mt-2">
                            <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                              <h6 class="m-0 font-weight-bold text-primary">${data['graph_name']}</h6>
                                <div class="dropdown no-arrow">
                                  <a class="dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    ☰
                                  </a>
                                  <div class="dropdown-menu dropdown-menu-right shadow animated--fade-in" aria-labelledby="dropdownMenuLink">
                                    <div class="dropdown-header">Action</div>
                                    <a class="dropdown-item" onclick="DeleteElement('graphs','${data['id']}')" href=''>Delete</a>
                                  </div>
                                </div>
                            </div>

                            <!-- Legend  -->
                            <div class="card-body">
                              <div class="chart-area" style="position: relative;">
                                <canvas id="graph_${data['id']}"></canvas>
                              </div>
                             <center>${data['first_data_serie']}</center>
                            </div>
                          
                          </div>`

    return (newGraph)


  }