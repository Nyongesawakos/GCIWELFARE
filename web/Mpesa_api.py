<link rel="stylesheet" type="text/css" media="screen" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<div class="card">
    <div class="card-body">
    <table id="example" class="table table-striped table-hover" style="width:95%">
      <thead>
        <table>  
            <thead>  
                <tr class="bg-primary">
                    <th class="bg-info">Month</th>
                    <th class="bg-info">Date</th>
                    <ul>
                    <th class="bg-info">Month</th>
                    <th class="bg-info">Date</th>
                        </ul>
                    
                </tr> 
            </thead>  
            <tbody>  
                {% for room in lists %}  
                    <tr>  
                        <td>{{ room.host }}</td>  
                        <td>{{ room.lastName }}</td>  
                        <td>  
                            <ul>  
                                {% for update in payment %}  
                                    <td><li>{{ update.code }}</li> </td> 
                                    <td><li>{{ update.amount }}</li> </td> 
                                {% endfor %}  
                            </ul>  
                        </td>  
                    </tr>  
                {% endfor %}  
            </tbody>  
    </tfoot>
</table>

       