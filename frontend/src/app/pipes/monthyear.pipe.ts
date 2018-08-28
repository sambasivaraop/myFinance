import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'monthyear'
})
export class MonthYearPipe implements PipeTransform {

  transform(value: any, month: string, year:number): any {
    return value.filter(payslip => ((payslip.month==month)&&(payslip.year==year)));
  }

}
