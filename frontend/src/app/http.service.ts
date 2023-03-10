import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private http: HttpClient) { 
  }

  // API ENDPOINTS:
  // "movies": "http://127.0.0.1:8000/api/v1/movies/",
  // "actors": "http://127.0.0.1:8000/api/v1/actors/"

  setVotes(movieId: any, movieVotes: any){
    return this.http.patch(`http://localhost:8000/api/v1/movies/${movieId}/`,{
      'votes':movieVotes
    })
  }
  getMovies(){
    return this.http.get("http://127.0.0.1:8000/api/v1/movies/")
  }

  getActors(){
    return this.http.get("http://127.0.0.1:8000/api/v1/actors/")
  }
 
}
