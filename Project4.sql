use mydb;
INSERT INTO `mydb`.`tutor` (`TutorID`, `CertDate`, `Status`) VALUES ('100', '2018-05-01', 'Active');
INSERT INTO `mydb`.`tutor` (`TutorID`, `CertDate`, `Status`) VALUES ('101', '2018-05-01', 'Temp Stop');
INSERT INTO `mydb`.`tutor` (`TutorID`, `CertDate`, `Status`) VALUES ('102', '2018-05-01', 'Dropped');
INSERT INTO `mydb`.`tutor` (`TutorID`, `CertDate`, `Status`) VALUES ('103', '2018-05-22', 'Active');
INSERT INTO `mydb`.`tutor` (`TutorID`, `CertDate`, `Status`) VALUES ('104', '2018-05-22', 'Active');
INSERT INTO `mydb`.`tutor` (`TutorID`, `CertDate`, `Status`) VALUES ('105', '2018-05-22', 'Temp Stop');
INSERT INTO `mydb`.`tutor` (`TutorID`, `CertDate`, `Status`) VALUES ('106', '2018-05-22', 'Active');
select * from tutor where `Status` = 'Active';
INSERT INTO `mydb`.`student`(`StudentID`,`Group`,`Read`) VALUES('3000','3','2.3');
INSERT INTO `mydb`.`student`(`StudentID`,`Group`,`Read`) VALUES('3001','2','5.6');
INSERT INTO `mydb`.`student`(`StudentID`,`Group`,`Read`) VALUES('3002','3','1.3');
INSERT INTO `mydb`.`student`(`StudentID`,`Group`,`Read`) VALUES('3003','1','3.3');
INSERT INTO `mydb`.`student`(`StudentID`,`Group`,`Read`) VALUES('3004','2','2.7');
INSERT INTO `mydb`.`student`(`StudentID`,`Group`,`Read`) VALUES('3005','4','4.8');
INSERT INTO `mydb`.`student`(`StudentID`,`Group`,`Read`) VALUES('3006','3','7.8');
INSERT INTO `mydb`.`student`(`StudentID`,`Group`,`Read`) VALUES('3007','4','1.5');
select `StudentID`, max(`read`) from student;
INSERT INTO `mydb`.`match history`(`MatchID`,`TutorID`,`StudentID`,`StartDate`) VALUES('1','100','3000','2018-01-10');
INSERT INTO `mydb`.`match history`(`MatchID`,`TutorID`,`StudentID`,`StartDate`,`EndDate`) VALUES('2','101','3001','2018-01-15','2018-05-15');
INSERT INTO `mydb`.`match history`(`MatchID`,`TutorID`,`StudentID`,`StartDate`,`EndDate`) VALUES('3','102','3002','2018-02-10','2018-03-01');
INSERT INTO `mydb`.`match history`(`MatchID`,`TutorID`,`StudentID`,`StartDate`) VALUES('4','106','3003','2018-05-28');
INSERT INTO `mydb`.`match history`(`MatchID`,`TutorID`,`StudentID`,`StartDate`,`EndDate`) VALUES('5','103','3004','2018-06-10','2018-06-15');
INSERT INTO `mydb`.`match history`(`MatchID`,`TutorID`,`StudentID`,`StartDate`,`EndDate`) VALUES('6','104','3005','2018-06-10','2018-06-28');
INSERT INTO `mydb`.`match history`(`MatchID`,`TutorID`,`StudentID`,`StartDate`) VALUES('7','104','3006','2018-06-10');
select `TutorID`, COUNT(*) As NumberOfTimesDuplicated from `match history` group by `TutorID` having count(*)>1;
select `TutorID` from tutor where `TutorID` not in (select `TutorID` from `match history`);
select count(*) from `match history` where MONTH(startdate) between 1 and 5;