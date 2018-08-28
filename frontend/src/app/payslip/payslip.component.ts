import { Component, OnInit } from '@angular/core';
import { PayslipService } from '../payslip.service';
import { DomSanitizer } from '@angular/platform-browser';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-payslip',
  templateUrl: './payslip.component.html',
  styleUrls: ['./payslip.component.css']
})
export class PayslipComponent implements OnInit {

  monthList = ["January","February","March","April","May","June","July","August","September","October","November","December"]
  yearList = [2018,2017,2016,2015,2014,2013,2012,2011,2010]
  public payslips = []
  public year;
  public month;
  date = new Date();
  public currentMonth = this.monthList[this.date.getMonth()];
  public currentYear = this.date.getFullYear();
  errorMsg;
  data;
  constructor(private _payslipservice: PayslipService, public sanitizer: DomSanitizer, private _loginservice: LoginService) { }
 
  ngOnInit() {
    this._loginservice.loginResponse
    .subscribe(
      data => this.data = JSON.parse(data),
      error => this.errorMsg = error.error,
      () =>     this._payslipservice.getSlip(this.data).subscribe(data => this.payslips = data)
    );

    this.month = this.currentMonth;
    this.year = this.currentYear;
  }
  onMonthChange(value){
    this.month = value;
  }
  onYearChange(value){
    this.year = value;
  }
  getSafeUrl(url){
    return this.sanitizer.bypassSecurityTrustResourceUrl(url);
  }
}
