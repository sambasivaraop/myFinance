import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { IInvestmentDetails } from './investmentdetails';
import { Investment } from './investment';
import { throwError} from 'rxjs';
import { catchError } from 'rxjs/operators';
import { LoginService } from './login.service';
import { Observable } from 'rxjs/internal/Observable';

@Injectable({
  providedIn: 'root'
})
export class InvestmentService {

  errorMsg;
  data;
  headers = new HttpHeaders();
  constructor(private _http: HttpClient, private _loginservice: LoginService) { 
    this._loginservice.loginResponse
    .subscribe(
      data => this.data = JSON.parse(data),
      error => this.errorMsg = error.error,
      () => this.set_header(this.data),
    );
  }
  
  private _investmentApi: string = 'http://127.0.0.1:8000/payroll/investment/';
  private _investmentGetApi: string = 'http://127.0.0.1:8000/payroll/investment/employee_investment_details/';

  set_header(data){
    this.headers = new HttpHeaders().set('Authorization', 'JWT '+data.token)
  }
  
  submit_investment(investment: Investment){
    return this._http.post<any>(this._investmentApi, investment,{headers: this.headers})
              .pipe(catchError(this.errorHandler))
  }
  errorHandler(error: HttpErrorResponse){
    return throwError(error);
  }

  get_investment(data): Observable<IInvestmentDetails[]>{
    this.headers = new HttpHeaders().set('Authorization', 'JWT '+data.token)
    return this._http.get<IInvestmentDetails[]>(this._investmentGetApi, {headers: this.headers});
  }
}
