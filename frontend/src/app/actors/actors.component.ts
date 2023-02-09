import { Component } from '@angular/core';
import { HttpService } from '../http.service';

@Component({
  selector: 'app-actors',
  templateUrl: './actors.component.html',
  styleUrls: ['./actors.component.css']
})
export class ActorsComponent {
  // Create an instance (_http) of the service
  actors : any;


  constructor(private httpService: HttpService) {}


  // When component loads (lifecycle hook)
  ngOnInit(){
    this.getActors();
  }

  getActors(){
    this.httpService.getActors().subscribe(
      data => {
        console.log(data); 
        this.actors = data;
        console.log(this.actors);
      }
    )
   
  }

}
