export default function getStudentIdsSum(studList) {
  const sumOfId = studList.reduce((acc, studPos) => acc + studPos.id,0,);
  return sumOfId;
}