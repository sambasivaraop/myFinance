import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule} from '@angular/forms'
import {HashLocationStrategy, LocationStrategy} from '@angular/common';
import { AppRoutingModule, routingComponents } from './app-routing.module';

import { AppComponent } from './app.component';
import { PayslipService } from './payslip.service';
import { HttpClientModule } from '@angular/common/http';
import { MonthYearPipe } from './pipes/monthyear.pipe';



@NgModule({
  declarations: [
    AppComponent,
    routingComponents,
    MonthYearPipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [PayslipService],
  bootstrap: [AppComponent]
})
export class AppModule { }
