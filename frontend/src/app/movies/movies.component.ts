import { Component } from '@angular/core';
import { HttpService } from '../http.service';


@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.css']
})
export class MoviesComponent {

  // TODO: On click of the +- btn, 
  // send a PATCH request to update the votes

  movies: any
  
  constructor(private httpService: HttpService) {}

  // When component loads (lifecycle hook)
  ngOnInit(){
    this.getMovies();
  }

  onSort(by : any){
    this.movies.sort((a :any, b : any) => {
      return a[by] < b[by]
    })
  }

  onVote(movieId :any, newVotes : any){
    console.log(movieId, newVotes); 
    this.httpService.setVotes(movieId, newVotes).subscribe(
      data => {
        console.log(data);
        this.getMovies();
        // return {...data, votes: newVotes}
      }
    )
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
