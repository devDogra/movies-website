import { Component } from '@angular/core';
import { HttpService } from '../http.service';


@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.css']
})
export class MoviesComponent {

  movies: any
  
  constructor(private httpService: HttpService) {}

  // When component loads (lifecycle hook)
  ngOnInit(){
    this.getMovies();
  }

  getMovies(){
    this.httpService.getMovies().subscribe(
      data => {
        console.log(data); 
        this.movies = data;
      }
    )
   
  }


}
